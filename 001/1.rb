def sum
  s = 0
  (0..999).each do |i|
    if (i % 3 == 0 || i % 5 == 0 || i % 15 == 0)
      s += i.to_i
    end
  end
  s
end

puts sum
