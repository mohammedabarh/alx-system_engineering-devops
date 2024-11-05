#!/usr/bin/env ruby
# Script Name: 2-repetition_token_1.rb
# Description: Matches 'htn' or 'hbtn' in the input text
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/hb?tn/).join
