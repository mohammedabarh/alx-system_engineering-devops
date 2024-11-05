#!/usr/bin/env ruby
# Script Name: 100-textme.rb
# Description: Extracts sender, receiver, and flags from TextMe log entries
# Author: Your Name
# Date: Current Date

# Regular expression breakdown:
# \[from:(.*?)\] - Captures sender information
# \[to:(.*?)\] - Captures receiver information
# \[flags:(.*?)\] - Captures flags
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
