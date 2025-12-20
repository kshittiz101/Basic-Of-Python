# Thermostat Warning System (With Device Status)

## Problem Statement

A smart home uses a thermostat warning system to monitor room temperature and provide alerts.  
However, the system should also handle cases where the thermostat device is not active.

Your task is to create a program that displays appropriate messages based on:
- Whether the thermostat device is active
- The current temperature (if the device is active)

## Conditions and Messages

### Device Status

- If the thermostat device is **not active**, display:  
  **"Device is not active"**

### Temperature Conditions (When Device Is Active)

| Temperature Range | Warning Message |
|------------------|-----------------|
| Below 10°C       | "Warning: Temperature too low" |
| 10°C to 25°C     | "Temperature is normal" |
| 26°C to 35°C     | "Warning: Temperature is high" |
| Above 35°C       | "Critical Alert: Temperature too high" |

## Task

- Take two inputs:
  1. A boolean value indicating whether the thermostat device is active (`true` or `false`)
  2. An integer representing the current temperature in Celsius
- If the device is not active, ignore the temperature and display the device status message.
- If the device is active, display a warning message based on the temperature.

## Input Format

- First input: boolean value (`true` or `false`)
- Second input: integer temperature in Celsius

## Output Format

- Display exactly one message based on the given conditions.

