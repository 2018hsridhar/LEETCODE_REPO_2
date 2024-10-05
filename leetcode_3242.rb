'''
99 cells maximium all disticnt grid values
'''
class NeighborSum

=begin
    :type grid: Integer[][]
=end
    def initialize(grid)
        @grid = grid
        @cadinalDirs = [
            [-1,0],[1,0],[0,-1],[0,1]
        ]
        @diagonalDirs = [
            [-1,1],[-1,-1],[1,1],[1,-1]
        ]
        @m = grid.length
        @n = grid[0].length
        @valMap = createVaueMap(grid)
    end

    def createVaueMap(grid)
        valMap = Hash.new
        (0...@m).each { |i|
            (0...@n).each { |j|
                val = grid[i][j]
                record = [i,j]
                valMap[val] = record
            }
        }
        return valMap
    end

=begin
    :type value: Integer
    :rtype: Integer
=end
# you ahve to find the index of thev alue
# hey I think I'm getting LC burnout call 
    def adjacent_sum(value)
        adjSum = 0
        record = @valMap[value]
        r = record[0]
        c = record[1]
        for dir in @cadinalDirs
            childR = r + dir[0]
            childC = c + dir[1]
            if(is_in_bounds(childR,childC))
                adjSum += @grid[childR][childC]
            end
        end
        return adjSum
    end


=begin
    :type value: Integer
    :rtype: Integer
=end
    def diagonal_sum(value)
        diagSum = 0
        record = @valMap[value]
        r = record[0]
        c = record[1]
        for dir in @diagonalDirs
            childR = r + dir[0]
            childC = c + dir[1]
            if(is_in_bounds(childR,childC))
                diagSum += @grid[childR][childC]
            end
        end
        return diagSum
    end

    def is_in_bounds(r,c)
        return (0 <= r && r < @m) && (0 <= c && c < @n)
    end


end

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum.new(grid)
# param_1 = obj.adjacent_sum(value)
# param_2 = obj.diagonal_sum(value)
