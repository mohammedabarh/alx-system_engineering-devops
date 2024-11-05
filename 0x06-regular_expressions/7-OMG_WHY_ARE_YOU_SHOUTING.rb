#!/usr/bin/env ruby
# Script Name: 7-OMG_WHY_ARE_YOU_SHOUTING.rb
# Description: Extracts and concatenates all capital letters from the input
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/[A-Z]/).join
