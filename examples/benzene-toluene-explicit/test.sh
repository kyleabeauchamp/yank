#!/bin/bash

if [ ! -e output ]; then
    echo "Making output directory..."
    mkdir output
fi

# Clean up any leftover files
echo "Cleaning up previous simulation..."
yank cleanup --store=output

# Set up calculation.
echo "Setting up binding free energy calculation..."
yank setup binding amber --setupdir=setup --ligname=BEN --store=output --iterations=1 --restraints=harmonic --temperature=300*kelvin --pressure=1*atmospheres --verbose

# Run the simulation with verbose output:
echo "Running simulation..."
yank run --store=output --verbose

