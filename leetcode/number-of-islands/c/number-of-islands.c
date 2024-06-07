void dfsMark(char** grid, int r, int c, int m, int* n);

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int count = 0;

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j] == '1') {
                dfsMark(grid, i, j, gridSize, gridColSize);
                count++;
            }
        }
    }
    return count;
}

void dfsMark(char** grid, int r, int c, int m, int* n) {
    if (
        r < 0 ||        
        c < 0 ||
        r == m ||
        c == *n ||
        grid[r][c] == '0'
    ) {
        return;
    }
    if (grid[r][c] == '1') {
        grid[r][c] = '0';
    }
    
    dfsMark(grid, r + 1, c, m, n);
    dfsMark(grid, r - 1, c, m, n);
    dfsMark(grid, r, c + 1, m, n);
    dfsMark(grid, r, c - 1, m, n);
}

