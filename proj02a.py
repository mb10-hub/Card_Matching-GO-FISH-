"""
Program: Card Game
Author: Marco Barragan
Description: The Program will be a card shuffling game
"""
from match_graphics import *


def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.

    TODO (Final): document the parameters and return value
    '''
    # TODO (Checkpoint A): implement the below logic
    #
    # The idea of how we shuffle is the following:
    # (1) shuffle the images
    # (2) pick out 12 of the images (these are the ones that will be pairs)
    # (3) pick out the 'extra image' (this is the one that will have no pair)
    # (4) create a list with 2 of each pair and the extra image
    # (5) shuffle that list

    shuffle(images)
    pick_cards = images[:12]
    extra_card = images[12]
    card_pairs = []
    for i in range(len(pick_cards)):
        card_pairs.append(pick_cards[i])
        card_pairs.append(pick_cards[i])
    card_pairs.append(extra_card)
    shuffle(card_pairs)
    print(card_pairs)

    # TODO (Checkpoint A): fix below.
    #
    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    v = 0
    cards = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(card_pairs[v])
            v += 1
        cards.append(row)
    return cards


def show_card(win, cards, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    # TODO (Checkpoint A ): finish this function as described
    #
    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_WIDTH, YMARGIN+CARD_HEIGHT)
    l_i = XMARGIN + CARD_WIDTH * i
    l_j = YMARGIN + CARD_HEIGHT * j
    w = CARD_WIDTH
    h = CARD_HEIGHT
    top_left = Point(l_j, l_i)
    bottom_right = Point(l_j + w, l_i + h)
    rect = Rectangle(top_left, bottom_right)
    rect.setFill('green')
    rect.setOutline('yellow')
    rect.setWidth(5)
    rect.draw(win)

    # TODO (Checkpoint A):
    # Draw the image for card_name at the center of the rectangle.
    card = Image(Point(l_j + 62.5, l_i + 62.5), cards[i][j])
    card.draw(win)
    return


def hide_card(win, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    # TODO (Checkpoint B): finish this function as described
    l_i = XMARGIN + CARD_WIDTH * i
    l_j = YMARGIN + CARD_HEIGHT * j
    w = CARD_WIDTH
    h = CARD_HEIGHT
    top_left = Point(l_j, l_i)
    bottom_right = Point(l_j + w, l_i + h)
    rect = Rectangle(top_left, bottom_right)
    rect.setFill('lightgreen')
    rect.setOutline('yellow')
    rect.setWidth(5)
    rect.draw(win)

    return


def mark_card(win, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j
    with a red X.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    # TODO (Checkpoint B): finish this function as described




    l_i = XMARGIN + CARD_WIDTH * i
    l_j = YMARGIN + CARD_HEIGHT * j
    w = CARD_WIDTH
    h = CARD_HEIGHT
    top_left = Point(l_j, l_i)
    bottom_right = Point(l_j + w, l_i + h)
    line = Line(top_left, bottom_right)
    line.setFill('red')
    line.setWidth(5)
    line.draw(win)

    top_right = Point(l_j + w, l_i)
    bottom_left = Point(l_j, l_i + h)
    line = Line(top_right, bottom_left)
    line.setFill('red')
    line.setWidth(5)
    line.draw(win)

    return


def get_col(x):
    '''
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value
    '''

    # TODO (Checkpoint B): finish this function as described
    m_point = x
    minus_m = m_point - YMARGIN
    div_m = minus_m // CARD_WIDTH
    if div_m >= 0 and div_m <= 4:
        return div_m
    else:
        return -1

    # return 0 idk what the -1 does or the 0 try both when get back to it ****** ******* ******* ****** *******


def get_row(y):
    '''
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    '''

    # TODO (Checkpoint B): finish this function as described

    m_point = y
    minus_x = m_point - XMARGIN
    div_x = minus_x // CARD_HEIGHT
    if div_x >= 0 and div_x <= 4:
        return div_x
    else:
        return -1



def main():
    '''
    TODO (Final): describe how your main function works.
    '''

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # draw the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            # For Checkpoint A, we place them face-up
            # show_card(win, cards, i, j)
            # For Checkpoint B, edit to place them face-down
            hide_card(win, i, j)
    # TODO (Checkpoint B): implement the below logic


    # until we win:
    # get a mouse click
    # figure out which card was clicked
    # if this is a 'first pick':
    # show the card
    # else, if this is a 'second pick':
    # show the card
    # wait 1 second
    # if we have a 'matched pair':
    # mark both pairs as matched (Final Code)
    # else:
    # hide both cards

    # if we got here, then we won
    # so, call the you_won function.
    '''
    m_point = win.getMouse()
    x_m_point = m_point.getX()
    y_m_point = m_point.getY()
    column_c = get_col(x_m_point)
    print(column_c)
    row_c = get_row(y_m_point)
    print(row_c)
    win.getMouse()
    '''
    matches_cards = []
    while True:
        try:

            for i in range(2):
                m_point = win.getMouse()
                x_m_point = m_point.getX()
                y_m_point = m_point.getY()
                column_c = int(get_col(x_m_point))
                print(column_c)
                row_c = int(get_row(y_m_point))
                print(row_c)

                while column_c == -1 or row_c == -1 or cards[row_c][column_c] in matches_cards:
                    m_point = win.getMouse()
                    x_m_point = m_point.getX()
                    y_m_point = m_point.getY()
                    column_c = int(get_col(x_m_point))
                    row_c = int(get_row(y_m_point))

                if i == 0:
                    show_card(win, cards, row_c, column_c)
                    first_click_row = row_c
                    first_click_col = column_c
                    print(cards)

                if i == 1:

                    while first_click_row == row_c and first_click_col == column_c:
                        m_point = win.getMouse()
                        x_m_point = m_point.getX()
                        y_m_point = m_point.getY()
                        column_c = int(get_col(x_m_point))
                        row_c = int(get_row(y_m_point))
                    show_card(win, cards, row_c, column_c)
                    second_click_row = row_c
                    second_click_col = column_c
                    game_delay(1)

            if cards[first_click_row][first_click_col] != cards[second_click_row][second_click_col]:
                hide_card(win, first_click_row, first_click_col)
                hide_card(win, second_click_row, second_click_col)
            else:
                mark_card(win, row_c, column_c)
                mark_card(win, first_click_row, first_click_col)
                matches_cards.append(cards[first_click_row][first_click_col])
                print(cards[first_click_row][first_click_col])
                if len(matches_cards) == 12:
                    you_won(win)

        except GraphicsError:
            exit(-1)


    win.getMouse()

main()