#!/bin/bash
a="manash"
echo $a
read -p "Which all letters you want to replace?:" rep
read -p "What you want to replace it with?:" wrep
b=${a/$rep/$wrep}
echo $b
