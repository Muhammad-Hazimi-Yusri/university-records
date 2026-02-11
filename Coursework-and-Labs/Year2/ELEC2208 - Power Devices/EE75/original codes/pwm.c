/*
 *  Simple program to generate six 50Hz PWM signals with 50% duty cycle and ~1uS deadtime
 *
 *  PORTB is used as the main output for PWM. PIN mapping is listed below
 *
 *  ilmatto          BLDC Testbed
 *  PIN A0     --       S1
 *  PIN A1     --       S2
 *  PIN A2     --       S3
 *  PIN A3     --       S4
 *  PIN A4     --       S5
 *  PIN A5     --       S6
 */

#ifndef TIMSK1
#define TIMSK1 TIMSK1
#endif

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define F_PWM 50				// Set the PWM frequency to 50Hz
#define DEAD_TIME 0.001			// Set the deadtime for mosfets to 1uS

#define DRIVE_PORT PORTA		// Port definition
#define DRIVE_DDR DDRA			// Port direction
#define PRESCALER 8				// Timer prescaler
#define F_CPU 12000000UL		// MCU running frequency

#define toggleS1 PINA |=_BV(0)
#define toggleS2 PINA |=_BV(1)
#define toggleS3 PINA |=_BV(2)
#define toggleS4 PINA |=_BV(3)
#define toggleS5 PINA |=_BV(4)
#define toggleS6 PINA |=_BV(5)

int x, n, d1, d2, d3;

void initialize();
void setFrequency();
void enableInterrupts();

/* Toggles the phases according to the Figure 1 */
ISR(TIMER1_COMPA_vect){

	n = x%3;

	if(n==0)
	{
		if(d1==1)
		{
			toggleS1;
			_delay_ms(DEAD_TIME);
			toggleS2;
			d1 = 0;
		}

		else
		{
			toggleS2;
			_delay_ms(DEAD_TIME);
			toggleS1;
			d1 = 1;
		}

		x = 1;
	}


	if(n==2)
	{
		if(d2==1)
		{
			toggleS3;
			_delay_ms(DEAD_TIME);
			toggleS4;
			d2 = 0;
		}

		else
		{
			toggleS4;
			_delay_ms(DEAD_TIME);
			toggleS3;
			d2 = 1;
		}
		x = 3;
	}


	if(n==1)
	{
		if(d3==1)
		{
			toggleS6;
			_delay_ms(DEAD_TIME);
			toggleS5;
			d3 = 0;
		}

		else
		{
			toggleS5;
			_delay_ms(DEAD_TIME);
			toggleS6;
			d3 = 1;
		}
		x = 2;
	}
}

int main(){

	d1 = 1; d2 = 1; d3 = 1; x = 0;

	// Configure the ports
	initialize();

	// Set the PWM frequency
	setFrequency();

	//Enable interrupts
	enableInterrupts();

	// call UART - use only for testing
	// init_debug_uart0();

	while(1){
	// ISR handles everything
	}

return(0);
}

/* port and timer configuration */
void initialize(){

	// set ports B to output
	DRIVE_DDR = 0xFF;

	// configure the timer
	TCCR1A = _BV( COM1A0 ) | _BV(WGM10);
	TCCR1B |=_BV(WGM13)|_BV(CS11);

	// set initial PWM output sequence
	DRIVE_PORT |= _BV(0) | _BV(2) | _BV(5);
	DRIVE_PORT &= ~_BV(1) & ~_BV(3) & ~_BV(4);
}

/* calculate the OCR1A value according to frequency */
void setFrequency(){

	// OCR1A value = 12000000/2*2*8/50*3 for 50Hz frequency
	OCR1A = (uint16_t)(F_CPU/(2*2*PRESCALER)/(F_PWM*3));
}

/* interrupt enable */
void enableInterrupts(){

	//enable interrupt on compare match
	TIMSK1 |= _BV(OCIE1A);

	//enable global interrupts
	sei();
}
