#!/bin/bash
count=$(find /etc -type f 2>/dev/null | wc -l)
echo "Кількість звичайних файлів у /etc: $count"
