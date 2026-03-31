#include <iostream>
#include <string>
#include <limits>
using namespace std;

#define BOARD_SIZE 9 

static bool is_winner(char player, char board[BOARD_SIZE]) {
    bool win = false;

    if (board[0] == player && board[1] == player && board[2] == player) {
        win = true;
    } else if (board[0] == player && board[4] == player && board[8] == player) {
        win = true;
    } else if (board[0] == player && board[3] == player && board[6] == player) {
        win = true;
    } else if (board[1] == player && board[4] == player && board[7] == player) {
        win = true;
    } else if (board[2] == player && board[4] == player && board[6] == player) {
        win = true;
    } else if (board[2] == player && board[5] == player && board[8] == player) {
        win = true;
    } else if (board[3] == player && board[4] == player && board[5] == player) {
        win = true;
    } else if (board[6] == player && board[7] == player && board[8] == player) {
        win = true;
    }

    return win; 
}

static void display_round_winner (char player) {
    cout << "----------------" << endl;
    cout << endl;
    cout << "Player " << player << " won this round!" << endl;
    cout << endl;
    cout << "----------------" << endl;
    cout << endl;
}

static void display_draw(){
    cout << "----------------" << endl;
    cout << endl;
    cout << "This round was a draw" << endl;
    cout << endl;
    cout << "----------------" << endl;
    cout << endl;
}

static void take_turn(
    char board[BOARD_SIZE],
    char player
) {
    int spot;
    bool invalid = true;

    while(invalid) {
        cout << "Which spot? ";
        cin >> spot;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout << "Not an integer. Try again." << endl;
        } else if (spot > 9 || spot < 1) {
            cout << "Invalid value. Try again." << endl;
        } else if (board[spot - 1] == 'X' || board[spot - 1] == 'O') {
            cout << "Invalid Spot. Try again." << endl;
        } else {
            invalid = false;
        }
    
    }

    board[(spot - 1)] = player;

}

static bool check_draw(char board[BOARD_SIZE]) {
    for (int i = 0; i < BOARD_SIZE; i++){
        if (board[i] != 'X' && board[i] != 'O') {
            return false;
        }
    }
    return true;

}

static void change_player(char &player) {
    player = (player == 'X' ? 'O' : 'X');  
}

static void draw_text(
    int player_wins[2],
    char player,
    int round   
) {
    cout << "Round: " << round << "\tPlayer X wins: " << player_wins[0] << endl;
    cout << "Player turn: " << player << "\tPlayer O wins: " << player_wins[1] << endl;
}

static void draw_board(char board[BOARD_SIZE]) {
    string offset = "\t";
    cout << offset << "     |     |      \n";
    cout << offset << "  " << board[0] << "  |  " << board[1] << "  |  " << board[2] << endl;
    cout << offset << "_____|_____|_____ \n";
    cout << offset << "     |     |      \n";
    cout << offset << "  " << board[3] << "  |  " << board[4] << "  |  " << board[5] << endl;
    cout << offset << "_____|_____|_____ \n";
    cout << offset << "     |     |      \n";
    cout << offset << "  " << board[6] << "  |  " << board[7] << "  |  " << board[8] << endl;
    cout << offset << "     |     |      \n";
    cout << offset << "\n";
}

static void draw(
    int player_wins[2], 
    char board[BOARD_SIZE],
    char player, 
    int round
) {
    draw_text(player_wins, player, round);
    draw_board(board);
}

static void round_winner(char player, int player_wins[2]) {
    change_player(player); // This is because player changes during rest of while loop
    
    if (player == 'X') { 
        player_wins[0] = player_wins[0] + 1;
    } else if (player == 'O') {
        player_wins[1] = player_wins[1] + 1;
    }
    display_round_winner(player);

}

static void init_board(char board[BOARD_SIZE]) {
    for (int i = 0; i < BOARD_SIZE; i++) {
        board[i] = 'I';
    }

    for (int i = 0; i < BOARD_SIZE; i++) {
    //ASCII 0 starts at 48, 9 is 57
        board[i] = (char)(i+49);
    }

}

static void check_winner(int player_wins[2], int min_rounds) {
    if (player_wins[0] >= min_rounds) {
        cout << "----------------" << endl;
        cout << endl;
        cout << "Player X won the game with " << player_wins[0] << " wins. Congradualations!" << endl;
        cout << endl;
        cout << "----------------" << endl;
        cout << endl;
    } else if (player_wins[1] >= min_rounds) {
        cout << "----------------" << endl;
        cout << endl;
        cout << "Player O won the game with " << player_wins[1] << " wins. Congradualations!" << endl;
        cout << endl;
        cout << "----------------" << endl;
        cout << endl;
    } else {
        cout << "----------------" << endl;
        cout << endl;
        cout << "The game ended on a draw!" << endl;
        cout << endl;
        cout << "----------------" << endl;
        cout << endl;
    }
}

static void round_loop(
    char board[BOARD_SIZE],
    char &player,
    int player_wins[2],
    int round
) {
    char Draw = false;

    while (!is_winner('X', board) && !is_winner('O', board) && !Draw) {
        take_turn(board, player);
        change_player(player);
        draw(player_wins, board, player, round);
        Draw = check_draw(board);
    }
    
    if (!Draw) {
        round_winner(player, player_wins);
    } else {
        display_draw();
    }
} 
    

extern void game_loop(int max_rounds) {
    char board[9];
    int player_wins[2] = {0, 0};
    int round = 1;
    // 3 / 2 = 1, 3 - 1 = 2 ... 5 / 2 = 2, 5 - 2 = 3 ... 7 / 2 = 3, 7 - 3 = 4
    int min_rounds = max_rounds - (max_rounds / 2);

    while (round <= max_rounds && player_wins[0] < min_rounds && player_wins[1] < min_rounds) {
        //game loop
        char player = 'X';

        init_board(board);
        draw(player_wins, board, player, round);

        //round loop
        round_loop(board, player, player_wins, round);

        round++;
        
        if (player_wins[0] < min_rounds && player_wins[1] < min_rounds) {
            cout << "Press Enter to continue to next round" << endl;
            string temp;
            getline(cin.ignore(), temp);
        }
    }

    check_winner(player_wins, min_rounds);

}