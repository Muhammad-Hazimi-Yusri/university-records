/*  Simple program for BLDC motor control. 
 *
 *  Students are required to finish the phase commutation section in order to spin the BLDC drive
 *
 *  Pin connections listed below:
 *
 *  ilmatto          BLDC Testbed
 *  PIN A0     --       S1
 *  PIN A1     --       S2
 *  PIN A2     --       S3
 *  PIN A3     --       S4
 *  PIN A4     --       S5
 *  PIN A5     --       S6
 *
 *  PIN C0     --      	Hall A
 *  PIN C1     --      	Hall B
 *  PIN A7     --      	Hall C
 *
 */

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include "debug.h"

// switch configuration
#define S1H PORTA |=  _BV(0)
#define S1L PORTA &= ~_BV(0)
#define S2H PORTA |=  _BV(1)
#define S2L PORTA &= ~_BV(1)
#define S3H PORTA |=  _BV(2)
#define S3L PORTA &= ~_BV(2)
#define S4H PORTA |=  _BV(3)
#define S4L PORTA &= ~_BV(3)
#define S5H PORTA |=  _BV(4)
#define S5L PORTA &= ~_BV(4)
#define S6H PORTA |=  _BV(5)
#define S6L PORTA &= ~_BV(5)

void initialize();
int readHall();

int hallA, hallB, hallC, phaseA = 0, phaseB = 0, phaseC = 0;

int main(){

	/* set up ports */
	initialize();

	while(1){

		/* read hall sensor values */
		readHall();
			
		/********************************  PHASE COMMUTATION  ****************************************/
		
		/* Compare the read hall values with all possible ones and set the correct phase output.
		 *
		 * -1 means phase is set to low
		 * 	0 means phase is off
		 * 	1 means phase is set to high
		 *
		 * Phase commutation is given for the first two hall sensor values 001 and 011 (for CCW rotation)
		 *		 
		 *	hallA	hallB	hallC	 phaseA		phaseB		phaseC
		 *	  0		  0		  1			0		  -1		   1
		 *	  0       1       1        -1	       0           1 
		 *   ...     ...
		 */
		 

		// hall sensor ABC value = 001
		if ((hallA == 0) && (hallB == 0) && (hallC != 0)){

			phaseA =  0;
			phaseB = -1;
			phaseC =  1;
		}

		// hall sensor ABC value = 011
		else if ((hallA == 0) && (hallB != 0) && (hallC != 0)){

			phaseA = -1;
			phaseB =  0;
			phaseC =  1;
		}

		/*	Student TODO list:	 
		 *   
		 *  1) 	Complete the phase commutation table for the other 4 hall sensor values (CCW rotation)
		 *		to drive the BLDC motor. Test your code.
		 *
		 *  2) 	Adjust the code to include CW rotation. Do not forget to include a small delay when 
		 * 		changing the direction of rotation while BLDC is operatonal. Otherwise it might damage 
		 *		the motor.  
		 */
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		/***********************************************************************************************/		
		

		/* Phase A configuration */
		switch (phaseA){

				// Phase A set to High
				case 1:
					S1H;
					S2L;
				break;

				// Phase A disabled
				case 0:
					S1L;
					S2L;
				break;

				// Phase A set to Low
				case -1:
					S1L;
					S2H;
				break;
		}

		/* Phase B configuration */
		switch (phaseB){

				// Phase B set to High
				case 1:
					S3H;
					S4L;
				break;

				// Phase B disabled
				case 0:
					S3L;
					S4L;
				break;

				// Phase B set to Low
				case -1:
					S3L;
					S4H;
				break;
		}

		/* Phase C configuration */
		switch (phaseC){

				// Phase C set to High
				case 1:
					S5H;
					S6L;
				break;

				// Phase C disabled
				case 0:
					S5L;
					S6L;
				break;

				// Phase C set to Low
				case -1:
					S5L;
					S6H;
				break;
		}
	}
return(0);
}


/****** Port configuration ******/
void initialize(){

	/* Set PORTA0-5 to output (for BLDC drive) */

	DDRA |= _BV(PA0);		// S1
	DDRA |= _BV(PA1);		// S2
	DDRA |= _BV(PA2);		// S3
	DDRA |= _BV(PA3);		// S4
	DDRA |= _BV(PA4);		// S5
	DDRA |= _BV(PA5);		// S6

	/* Set PC0, PC1, PA7 for hall sensor input*/

	DDRC &= ~_BV(PC0); 		// hall sensor A input
	PORTC |= _BV(PC0); 		// Enable pull-up on PC0 (might not be needed if external pull-up is used)

	DDRC &= ~_BV(PC1); 		// hall sensor B input
	PORTC |= _BV(PC1); 		// Enable pull-up on PC1 (might not be needed if external pull-up is used)

	DDRA &= ~_BV(PA7); 		// hall sensor C input
	PORTA |= _BV(PA7); 		// Enable pull-up on PA7 (might not be needed if external pull-up is used)

	init_debug_uart0();		// initialize UART for testing, requires debug.h header file to work

}

/****** Sample the hall sensor ******/
int readHall(){

	hallA	= (PINC & _BV(PC0));
	hallB	= (PINC & _BV(PC1));
	hallC	= (PINA & _BV(PA7));

	return (hallA & hallB & hallC);
}

