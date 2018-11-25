#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void printMatrix(int**, int, int);
int** findInitialDegrees(const int, const int);
int** knightsTour(int, int, int, int);
bool tourIsValid(int**, int, int);

int main()
{
    srand(time(0));

    int boardHeight = 5;
    int boardWidth = boardHeight;

    cout << endl << "-----------------"
         << endl << "|Board size: " << boardHeight << "x" << boardWidth << "|"
         << endl << "-----------------" << endl;

    for (int startRow = 0; startRow < boardHeight; startRow++)
    {
        for (int startCol = 0; startCol < boardWidth; startCol++)
        {
            cout << "Starting at square " << startRow + 1 << ", " << startCol + 1 << "..." << endl;

            int** solution = knightsTour(boardHeight, boardWidth, startRow, startCol);

            if (tourIsValid(solution, boardHeight, boardWidth))
                cout << "Tour complete:" << endl;
            else
                cout << "Tour failed. Progress:" << endl;

            printMatrix(solution, boardHeight, boardWidth);
            cout << endl;
        }
    }

    for (boardHeight = 6; boardHeight <= 8; boardHeight += 2)
    {
        boardWidth = boardHeight;

        cout << endl << "-----------------"
             << endl << "|Board size: " << boardHeight << "x" << boardWidth << "|"
             << endl << "-----------------" << endl;

        for (int i = 0; i < 4; i++)
        {
            //Pick four random starting points - they may sometimes be the same
            int startRow = rand() % boardHeight;
            int startCol = rand() % boardWidth;

            cout << "Starting at square " << startRow + 1 << ", " << startCol + 1 << "..." << endl;

            int** solution = knightsTour(boardHeight, boardWidth, startRow, startCol);

            if (tourIsValid(solution, boardHeight, boardWidth))
                cout << "Tour complete:" << endl;
            else
                cout << "Tour failed. Progress:" << endl;

            printMatrix(solution, boardHeight, boardWidth);
            cout << endl;
        }
    }
}

int** knightsTour(int numRows, int numCols, int rowPosition, int colPosition)
{
    int** degrees = findInitialDegrees(numRows, numCols);

    //Initialize board
    int** moves = new int*[numRows];
    for (int row = 0; row < numRows; row++)
    {
        moves[row] = new int[numCols];
        for (int col = 0; col < numCols; col++)
            moves[row][col] = -1;
    }
    moves[rowPosition][colPosition] = 1;

    int numMoves = 1;
    while (true)
    {
        numMoves++;
        int nextMoveRow = -1;
        int nextMoveCol = -1;

        //Check for the best move
        if (rowPosition - 2 >= 0)
        {
            if (colPosition - 1 >= 0)
            {
                int row = rowPosition - 2;
                int col = colPosition - 1;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
            if (colPosition + 1 < numCols)
            {
                int row = rowPosition - 2;
                int col = colPosition + 1;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
        }
        if (rowPosition + 2 < numRows)
        {
            if (colPosition - 1 >= 0)
            {
                int row = rowPosition + 2;
                int col = colPosition - 1;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
            if (colPosition + 1 < numCols)
            {
                int row = rowPosition + 2;
                int col = colPosition + 1;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
        }
        if (colPosition - 2 >= 0)
        {
            if (rowPosition - 1 >= 0)
            {
                int row = rowPosition - 1;
                int col = colPosition - 2;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
            if (rowPosition + 1 < numRows)
            {
                int row = rowPosition + 1;
                int col = colPosition - 2;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
        }
        if (colPosition + 2 < numCols)
        {
            if (rowPosition - 1 >= 0)
            {
                int row = rowPosition - 1;
                int col = colPosition + 2;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
            if (rowPosition + 1 < numRows)
            {
                int row = rowPosition + 1;
                int col = colPosition + 2;
                int degree = degrees[row][col];
                if (degree > 0 && moves[row][col] == -1
                        && (nextMoveRow == -1 || degree < degrees[nextMoveRow][nextMoveCol]))
                {
                    nextMoveRow = row;
                    nextMoveCol = col;
                }
            }
        }

        if (nextMoveRow > -1 && nextMoveCol > -1)
        {
            moves[nextMoveRow][nextMoveCol] = numMoves;

            //Decrement degrees
            if (rowPosition - 2 >= 0)
            {
                if (colPosition - 1 >= 0)
                    degrees[rowPosition-2][colPosition-1]--;
                if (colPosition + 1 < numCols)
                    degrees[rowPosition-2][colPosition+1]--;
            }
            if (rowPosition + 2 < numRows)
            {
                if (colPosition - 1 >= 0)
                    degrees[rowPosition+2][colPosition-1]--;
                if (colPosition + 1 < numCols)
                    degrees[rowPosition+2][colPosition+1]--;
            }
            if (colPosition - 2 >= 0)
            {
                if (rowPosition - 1 >= 0)
                    degrees[rowPosition-1][colPosition-2]--;
                if (rowPosition + 1 < numRows)
                    degrees[rowPosition+1][colPosition-2]--;
            }
            if (colPosition + 2 < numCols)
            {
                if (rowPosition - 1 >= 0)
                    degrees[rowPosition-1][colPosition+2]--;
                if (rowPosition + 1 < numRows)
                    degrees[rowPosition+1][colPosition+2]--;
            }

            rowPosition = nextMoveRow;
            colPosition = nextMoveCol;
        }
        else
            break; //If there is no move to make, the tour has either completed or failed
    }

    return moves;
}

int** findInitialDegrees(const int numRows, const int numCols)
{
    int** board = new int*[numRows];
    for (int row = 0; row < numRows; row++)
    {
        board[row] = new int[numCols];

        for (int col = 0; col < numCols; col++)
        {
            board[row][col] = 0;

            if (row - 2 >= 0)
            {
                if (col - 1 >= 0)
                    board[row][col]++;
                if (col + 1 < numCols)
                    board[row][col]++;
            }
            if (row + 2 < numRows)
            {
                if (col - 1 >= 0)
                    board[row][col]++;
                if (col + 1 < numCols)
                    board[row][col]++;
            }
            if (col - 2 >= 0)
            {
                if (row - 1 >= 0)
                    board[row][col]++;
                if (row + 1 < numRows)
                    board[row][col]++;
            }
            if (col + 2 < numCols)
            {
                if (row - 1 >= 0)
                    board[row][col]++;
                if (row + 1 < numRows)
                    board[row][col]++;
            }
        }
    }

    return board;
}

void printMatrix(int** matrix, int height, int width)
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (matrix[i][j] > 0)
                cout << matrix[i][j] << "\t";
            else
                cout << "-" << "\t";
        }
        cout << endl;
    }
}

bool tourIsValid(int** board, int numRows, int numCols)
{
    for (int i = 0; i < numRows; i++)
        for (int j = 0; j < numCols; j++)
            if (board[i][j] <= 0)
                return false;

    return true;
}
