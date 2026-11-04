require 'liquid'

module Jekyll
  module ArrayFilters
    # filter out empty and trim entries in array
    def array_filter(array)
      return array
        .map{|x| x.is_a?(String) ? x.strip() : x}
        .select{|x| x and x != ""}
    end

    # omit middle items of array with ellipsis, leave N items on either side
    def array_carve(array, length = 3)
      if array.length <= length * 2
        return array
      else
        left = array.slice(0, length) || []
        right = array.slice(-length, length) || []
        return [left, "...", right].flatten()
      end
    end
    # like array_carve, but always keep entries containing any of the given names
    def array_carve_keep(array, length = 3, names = [])
      names = Array(names)
      keep = array.each_index.select do |i|
        i < length || i >= array.length - length ||
          names.any? { |n| array[i].to_s.include?(n) }
      end
      result = []
      prev = -1
      keep.each do |i|
        result << "..." if i > prev + 1
        result << array[i]
        prev = i
      end
      result
    end
  end
end

Liquid::Template.register_filter(Jekyll::ArrayFilters)
