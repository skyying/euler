def f
  prev = 1
  current = 2
  s = 0

  while current < 4000000
    if current % 2 == 0
      puts current
      s += current
    end
    prev, current = current, prev + current
  end
  s
end

puts "ans: #{f}"
