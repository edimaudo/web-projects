require 'rest-client'

print "what would you like to search for: "
response = gets.chomp
response = response.split.join("+")

client = RestClient.get("https://www.google.com/#q=#{response}")

puts
puts "Code:"
puts client.code
puts
puts "Cookies:"
puts client.cookies
puts
puts "Headers:"
puts client.headers
puts
puts "Body:"
puts client.body
