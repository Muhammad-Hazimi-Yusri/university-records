#include "app.h"
#include "tran.h"
#include "uart.h"

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <string.h>
#include <stdlib.h>

// Initialize hardware
void initializeAppHardware() {
  // Initialize LED
  // Initialize button
  // Initialize UART
}

// Main loop
void appCheck() {
    // Check button state
    // Check UART data
}

// Handle "IPPLS" request
void handleIPPLSRequest() {
  // Broadcast "IPPLS" request
  // Handle received "IPPLS" request
}

// Maintain hostname-IP address table
void maintainHostnameIPTable() {
  // Add hostname-IP pair to table
  // Resolve hostname to IP address
}

// Implement UART cli
void implementUARTCli() {
  // Parse received command
  // Perform appropriate action
}

// Interface with TRAN Layer
void interfaceWithTRANLayer() {
  // Provide necessary data to TRAN Layer
}