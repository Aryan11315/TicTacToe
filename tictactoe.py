import streamlit as st
import numpy as np

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.full((3,3), " ")
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board, player):
    for i in range(3):
        if np.all(board[i,:] == player) or np.all(board[:,i] == player):
            return True
    if (board[0,0] == board[1,1] == board[2,2] == player) or (board[0,2] == board[1,1] == board[2,0] == player):
        return True
    return False

def is_draw(board):
    return np.all(board != " ")

def handle_click(row, col):
    if st.session_state.game_over:
        return
    if st.session_state.board[row, col] == " ":
        st.session_state.board[row, col] = st.session_state.current_player

        # Check for winner
        if check_winner(st.session_state.board, st.session_state.current_player):
            st.session_state.game_over = True
            st.session_state.winner = st.session_state.current_player
        elif is_draw(st.session_state.board):
            st.session_state.game_over = True
            st.session_state.winner = "Draw"
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# ---------------- STREAMLIT UI ----------------
st.title("🎮 Tic Tac Toe")
st.write("Play a simple Tic Tac Toe game!")

# Display board as 3x3 grid of buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.session_state.board[i, j] == " ":
                if st.button(" ", key=f"{i}{j}"):
                    handle_click(i, j)
            else:
                st.button(st.session_state.board[i, j], key=f"{i}{j}", disabled=True)

# Show status
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.success("It's a draw! 🤝")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Current Turn: Player {st.session_state.current_player}")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.board = np.full((3,3), " ")
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

                
