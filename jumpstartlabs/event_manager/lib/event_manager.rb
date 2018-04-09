#event engagement app - A number of people have registered for an upcoming event. She has asked for your help in engaging these future attendees.
require "csv"
puts "EventManager initialized."

contents = CSV.open "event_attendees.csv", headers: true, header_converters: :symbol
contents.each do |row|
  name = row[:first_name]
  zipcode = row[:zipcode]
  puts "#{name} #{zipcode}"
end

=beginlines = File.readlines "event_attendees.csv"
lines.each do |line|
  next if line == " ,RegDate,first_Name,last_Name,Email_Address,HomePhone,Street,City,State,Zipcode\n"
  columns = line.split(",")
  name = columns[2]
  puts name
end=end

#read file methods
#contents = File.read "event_attendees.csv"
#puts contents

=beginlines = File.readlines "event_attendees.csv"
lines.each do |line|
  puts line
end=end

