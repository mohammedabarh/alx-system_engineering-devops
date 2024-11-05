#!/usr/bin/env ruby
# Script Name: 4-repetition_token_3.rb
# Description: Matches 'hb' followed by zero or more 't's and ending with 'n'
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/hbt*n/).join
