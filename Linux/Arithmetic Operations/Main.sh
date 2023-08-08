read expression
echo "$expression" | bc -l | xargs printf "%.3f"