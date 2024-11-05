#!/usr/bin/env ruby
# Script Name: 5-beginning_and_end.rb
# Description: Matches strings that start with 'h', end with 'n', 
#             and have exactly one character in between
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/h.n/).join
