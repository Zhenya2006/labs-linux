#!/bin/bash

COUNT=0

for ITEM in /etc/*; do
    if [ -f "$ITEM" ]; then
        COUNT=$((COUNT + 1))
    fi
done

echo "Кількість звичайних файлів у /etc: $COUNT"
