#!/usr/bin/env ruby
# Script Name: 3-repetition_token_2.rb
# Description: Matches 'hb' followed by one or more 't's and ending with 'n'
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/hbt+n/).join
