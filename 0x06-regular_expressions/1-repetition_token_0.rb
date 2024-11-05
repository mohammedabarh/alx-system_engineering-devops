#!/usr/bin/env ruby
# Script Name: 1-repetition_token_0.rb
# Description: Matches strings with 'hb', followed by 2-5 't's, and ending with 'n'
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/hbt{2,5}n/).join
