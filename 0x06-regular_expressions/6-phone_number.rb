#!/usr/bin/env ruby
# Script Name: 6-phone_number.rb
# Description: Matches exactly 10 digit phone numbers
# Author: Your Name
# Date: Current Date

puts ARGV[0].scan(/^\d{10}$/).join
