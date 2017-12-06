import random
import math
import time
import NeuralN

class Checkers:
    # Boolean True sets up the pieces on the game board. Boolean False does not.
    def __init__(self, boolean):
        self.gui_player = ""

        self.whiteNNW = [0.3196966466,0.2534705791,-0.0551931159,0.0042419175,-0.3452001349,-0.1370994661,0.4608760546,-0.1620046521,-0.1066212886,-0.3055779462,0.6119275751,0.7394049799,-0.2070229839,-0.3598332492,0.1944400975,-0.6567889655,0.119268897,0.4751672117,-0.2953071539,-0.1709250283,0.1447836713,-0.4372191956,-0.0345947496,0.1128665979,0.5295950944,0.3775151133,-0.493099124,-0.5246924562,-0.3863832244,0.1408622055,0.5224627614,-0.5657959541,0.5307768566,0.0884282007,-0.4347934114,-0.2832132995,0.0070207194,-0.2592281483,0.2594218309,-0.6982380881,-0.0080399571,0.2879223525,-0.7041922602,-0.1831983405,-0.6021472426,0.2259089662,0.6898595418,-0.5282751464,0.1866106569,0.3980530335,-0.4588905018,-0.1299839411,-0.630079722,-0.4830512572,0.2913984713,-0.4685670126,-0.0162637073,0.7876594007,-0.1915679594,-0.0087329798,0.0935282479,0.5962314975,0.4674877601,0.5566589236,-0.1243348143,-0.0932097361,-0.1127442309,0.4439872705,0.291858549,0.7231811734,0.1166014017,-0.4891462569,-0.7909035918,-0.3002018936,0.2538514405,0.5546757301,-0.0841019453,-0.6868767401,0.3138567605,-0.1133102772,-0.0073524166,0.4843156885,0.3595874285,0.2871697708,0.5922639664,-0.8298917656,0.1735193926,0.0072013571,-0.4298265012,0.7975170943,-0.0603039278,0.1387235773,0.1457814798,0.4700942618,0.2167850183,0.259804389,0.6125320084,0.4784704681,-0.7840900774,0.2145184854,-0.3882673473,-0.8431176995,0.1884380707,-0.2614306034,-0.2507501448,0.6819592461,0.1357472714,-0.1995736661,-0.390207953,0.1524033093,-0.670920729,-0.4119454251,0.622863565,0.4249016136,0.2886535688,0.3038373795,0.2761512435,0.4312113423,-0.0894073582,0.1336325248,-0.1391742409,0.0401607174,0.0045357919,0.1358486852,-0.1955992494,0.1861582107,-0.458720126,-0.0303386542,-0.4625507641,0.0471060251,0.5273460421,-0.0585655998,0.5614545255,0.1340194499,0.2011108292,0.2978112123,-0.7988419801,-0.3948510104,-0.2057178302,0.260161018,0.4964726152,0.0151025472,0.0327250969,0.7386021924,-0.2465967649,-0.7184163283,-0.5543244062,0.1663796102,-0.4468439039,0.026919731,0.10366951,0.4867795086,-0.1082709757,-0.308265595,-0.2676719168,-0.1730459687,0.1430869131,0.6671243943,0.2223136628,0.2800632064,-0.6730798977,-0.2489198172,-0.0066325771,0.4060372389,-0.1549623971,0.4866850517,-0.1767350559,0.4227561085,0.1374409576,0.0306672777,1.0207432018]
        self.blackNNW = [-1.215584084,-0.1488816789,-0.1999812783,0.1302523086,-0.2015380353,0.9809160972,-0.7990057989,-0.4804387362,0.0608032692,0.2735263026,0.0917098159,1.0134496274,1.3245855092,-0.1544941286,0.0754553545,-0.6834290121,-0.1908335738,-0.7429071092,-0.1558048579,-0.8216059584,-0.1012913466,0.8694193611,-0.0531293546,-0.1345915319,-0.5514468064,-0.6582544588,-0.4174257735,-0.896619704,-0.4963698571,0.9123754831,0.4555748277,-0.0426437038,0.2129071851,0.6610400388,-0.0314454624,-0.921150269,0.167292232,0.1001080115,0.5305665859,-0.7432755884,0.5519755942,0.3425446436,-0.6601779391,0.5411883235,0.5400123693,-0.5088741644,0.2764260383,-0.5834552044,-0.0583208943,-0.1695300181,0.0132719632,-0.5505019221,0.296583367,-0.7975040433,0.0475477204,0.645703263,-0.9685811936,0.4801427958,-0.6845825868,0.1275450607,0.6412027762,-1.1119338621,0.3619161973,0.0452459431,-0.4221256098,0.6980418059,0.1576714023,-0.0767202481,0.7077458519,-0.1395939402,-0.6357299878,-0.6817084386,-0.7012887532,0.0871283495,0.5239623585,-0.844040032,-0.6299885503,-0.2012147194,1.7747340765,-0.4824674103,-0.486949392,-0.0179172868,0.0286422392,-0.2317285363,0.7053384867,-0.9815871115,0.5826227527,0.0805191783,0.0528415556,0.2593988961,0.5655284589,0.2016683815,0.4884337481,-0.3103640336,-0.1640558678,-0.2863149768,0.2682081797,0.253097843,-0.1642187726,-0.3639842468,0.8767124876,0.1783389401,-0.4830741396,-0.1952455145,0.8927939633,-0.2338628566,0.761980542,0.4625287624,0.4082321156,0.1176911697,-0.3527261326,0.0949060464,0.8389308011,-0.9917983873,-0.6433539902,0.2020636026,0.5671116596,0.0188124792,-0.2197986755,0.4760750163,-0.4841573767,0.3346475777,0.7087065805,0.5371725184,0.691120365,0.3394925964,0.5426142002,0.2383292494,-0.7115284038,-1.1865275408,0.0280326719,0.4167810347,0.4783256687,-0.5001028057,-0.4539642774,-0.2123771796,-0.2669073709,0.6006945378,-0.0628273979,-0.7397875796,0.444195847,0.401444821,0.0005792213,0.6417745983,0.007048323,-0.382181254,0.5345896395,0.1665213657,-0.1626479955,0.9534807532,-0.3421035284,-0.0713540005,-0.1374478125,-0.3405718126,0.6032753175,-0.0858520735,0.422827201,-0.252731114,0.3678028782,0.2117247106,0.8392156306,0.1760727445,0.1037703726,0.6088282368,0.4670920787,0.0837600762,-0.259737468,0.1041640176,1.0517851646,-0.6986834705,-0.0026286412]
        self.whiteNN = NeuralN.NeuralNetwork()
        self.blackNN = NeuralN.NeuralNetwork()
        self.whiteNN.updateWeights(self.whiteNNW)
        self.blackNN.updateWeights(self.blackNNW)

        self.board_vector = [0 for i in range(32)]
        if boolean:
            self.__setBoard()

    # Sets the pieces on the board to all initial positions.
    def __setBoard(self):
        for i in range(12):
            self.board_vector[i] = 1
        for i in range(12, 20):
            self.board_vector[i] = 0
        for i in range(20, 32):
            self.board_vector[i] = -1
            
    def showBoardIndices(self):
        print("Board Indices")
        output = [[i for i in range(4)] for j in range(8)]
        k = 31
        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = k
                k -= 1
        for i in range(8):
            output[i] = output[i][::-1]
        
        k = 0
        print("  "+chr(9135)*18)
        for i in output:
            print("  "+chr(9122), end='')
            if k % 2 == 0:
                print("  ", end='')
            for j in i:
                if j == 31 or j == 23 or j == 15 or j == 7:
                    print(str(j), end='')
                else:
                    print(str(j)+ "  ", end='')
                if j < 10: 
                    print(" ", end='')
            print(chr(9130))
            k += 1
        print("  "+chr(9146) * 18)
    
    # prints board to standard output
    def showBoard(self, brdcpy):
        output = [0 for i in range(64)]
        for i in range(32):
            if(0 <= (i % 8) < 4):
                output[i*2] = brdcpy[i]
            else:
                output[(i*2)+1] = brdcpy[i]
    
        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if(output[i] == 1):
                board[i//8][i%8] = "w"
            elif(output[i] == -1):
                board[i // 8][i % 8] = "b"
            elif(output[i] == 2):
                board[i // 8][i % 8] = "W"
            elif(output[i] == -2):
                board[i // 8][i % 8] = "B"
            else:
                board[i // 8][i % 8] = "0"
        for i in range(7, -1, -1):
            print(board[i])
    
    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV2(self):
        output = [0 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]
    
        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = "w"
            elif (output[i] == -1):
                board[i // 8][i % 8] = "b"
            elif (output[i] == 2):
                board[i // 8][i % 8] = "W"
            elif (output[i] == -2):
                board[i // 8][i % 8] = "B"
            else:
                board[i // 8][i % 8] = "_"
    
        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i-7))] = board[i]
    
        print("-"*41)
        for i in range(8):
            print("|     ", end='')
            for j in board2[i]:
                print(j, "  ", end='')
            print("  |")
            print("|     ", end='')
            if(i%2 == 0):
                print("    ", end='')
            for k in range(int((math.fabs(i-8)*4)-4), int(math.fabs(i-8)*4), 1):
                print(k,"   ", end='')
                if(k % 8 == 7):
                    if(k == 7):
                        print(" ", end='')
                elif(k % 8 == 3):
                    if(k == 3 ):
                        print("     ", end='')
                    else:
                        print("    ", end='')
                elif(k < 10):
                    print("   ", end='')
                else:
                    print("  ", end='')
            print("|")
        print("-" * 41)
        
    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV2_5(self):
        output = [99 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]
    
        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = chr(9863)
            elif (output[i] == -1):
                board[i // 8][i % 8] = chr(9865)
            elif (output[i] == 2):
                board[i // 8][i % 8] = chr(9450)
            elif (output[i] == -2):
                board[i // 8][i % 8] = chr(9471)
            elif (output[i] == 0):
                board[i // 8][i % 8] = chr(9633)
            else:
                board[i // 8][i % 8] = chr(9632)
    
        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i-7))] = board[i]
    
        print("-"*41)
        for i in range(8):
            print("|     ", end='')
            for j in board2[i]:
                print(j, "  ", end='')
            print("  |")
            print("|     ", end='')
            if(i%2 == 0):
                print("    ", end='')
            for k in range(int((math.fabs(i-8)*4)-4), int(math.fabs(i-8)*4), 1):
                print(k,"   ", end='')
                if(k % 8 == 7):
                    if(k == 7):
                        print(" ", end='')
                elif(k % 8 == 3):
                    if(k == 3 ):
                        print("     ", end='')
                    else:
                        print("    ", end='')
                elif(k < 10):
                    print("   ", end='')
                else:
                    print("  ", end='')
            print("|")
        print("-" * 41)
        
    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV3(self):
        output = [99 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]
    
        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = chr(9863)
            elif (output[i] == -1):
                board[i // 8][i % 8] = chr(9865)
            elif (output[i] == 2):
                board[i // 8][i % 8] = chr(9450)
            elif (output[i] == -2):
                board[i // 8][i % 8] = chr(9471)
            elif (output[i] == 0):
                board[i // 8][i % 8] = chr(9633)
            else:
                board[i // 8][i % 8] = chr(9632)
    
        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i-7))] = board[i]
    
        print("  " + chr(9135)*18)
        for i in range(8):
            #print(str((i-7)*-1) + " ", end="")
            print("  ", end='')
            print(chr(9122), end='')
            for j in board2[i]:
                print(j+" ", end='')
            print(chr(9130))
        print("  " + chr(9146) * 18)
    
    # variable "type" is an integer denoting the type of piece. 1 for normal piece 2 for King.
    # variable "p" is an array of the current board positions
    def findSingleMoves(self, p, player_type):
        moves = []
        for i in range(32):
            lm = -1; rm = -1
            if 28 <= i < 32:
                lm = -1; rm = -1
            elif 0 <= (i % 8) < 4:
                if(p[i+4] == 0 and p[i] == player_type):
                    rm = i + 4
                if (i % 8) == 0:
                    lm = -1
                else:
                    if(p[i+3] == 0 and p[i] == player_type):
                        lm = i + 3
            elif 4 <= (i % 8) < 8:
                if(p[i+4] == 0 and p[i] == player_type):
                    lm = i + 4
                if (i % 8) == 7:
                    rm = -1
                else:
                    if(p[i+5] == 0 and p[i] == player_type):
                        rm = i + 5
            moves.append([i, [lm, rm]])
        return moves
    
    # variable "type" is an integer denoting the type of piece. -1 for normal piece -2 for King.
    # variable "p" is an array of the current board positions
    def findSingleMovesReverse(self, p, player_type):
        moves = []
        for i in range(32):
            lm = -1; rm = -1
            if 0 <= i < 4:
                lm = -1; rm = -1
            elif 0 <= (i % 8) < 4:
                if(p[i-4] == 0 and p[i] == player_type):
                    lm = i - 4
                if (i % 8) == 0:
                    rm = -1
                else:
                    if(p[i-5] == 0 and p[i] == player_type):
                        rm = i - 5
            elif 4 <= (i % 8) < 8:
                if(p[i-4] == 0 and p[i] == player_type):
                    rm = i - 4
                if (i % 8) == 7:
                    lm = -1
                else:
                    if(p[i-3] == 0 and p[i] == player_type):
                        lm = i - 3
            moves.append([i, [lm, rm]])
        return moves
    
    # Calculates all possible forward jump moves for a single piece.
    # Returns moves as a list of the form; [lm, rm]
    def findJumpsSinglePiece(self, p, indx, player_type):
        lm = -1
        rm = -1
        i = indx
        if 24 <= i < 32:
            lm = -1; rm = -1
        elif 0 <= (i % 8) < 4:
            if (i%8) == 3:
                rm = -1
            else:
                if(p[i] == player_type and (p[i+4]*p[i]) < 0 and p[i+9] == 0):
                    rm = i + 9
                else:
                    rm = -1
            if (i%8) == 0:
                lm = -1
            else:
                if (p[i] == player_type and (p[i + 3]*p[i]) < 0 and p[i+7] == 0):
                    lm = i + 7
                else:
                    lm = -1
        elif 4 <= (i % 8) < 8:
            if (i%8) == 7:
                rm = -1
            else:
                if (p[i] == player_type and (p[i + 5]*p[i]) < 0 and p[i+9] == 0):
                    rm = i + 9
                else:
                    rm = -1
            if (i%8) == 4:
                lm = -1
            else:
                if (p[i] == player_type and (p[i + 4]*p[i]) < 0 and p[i+7] == 0):
                    lm = i + 7
                else:
                    lm = -1
        return [lm, rm]
    
    # Returns a list of all possible forward jump moves of the form; [[0, [lm, rm]], [1, [lm, rm]]]
    def findJumps(self, p, player_type):
        moves = []
        for i in range(32):
            m_arr = self.findJumpsSinglePiece(p, i, player_type)
            moves.append([i, m_arr])
        return moves
    
    # Calculates all possible reverse jump moves for a single piece.
    # Returns moves as a list of the form; [lm, rm]
    def findJumpsReverseSinglePiece(self, p, indx, player_type):
        lm = -1
        rm = -1
        i = indx
        if 0 <= i < 8:
            lm = -1; rm = -1
        elif 0 <= (i % 8) < 4:
            if (i%8) == 3:
                lm = -1
            else:
                if (p[i] == player_type and (p[i-4]*p[i]) < 0 and p[i-7] == 0):
                    lm = i - 7
                else:
                    lm = -1
            if (i%8) == 0:
                rm = -1
            else:
                if(p[i] == player_type and (p[i-5]*p[i]) < 0 and p[i-9] == 0):
                    rm = i - 9
                else:
                    rm = -1
        elif 4 <= (i % 8) < 8:
            if (i%8) == 7:
                lm = -1
            else:
                if (p[i] == player_type and (p[i-3]*p[i]) < 0 and p[i-7] == 0):
                    lm = i - 7
                else:
                    lm = -1
            if (i%8) == 4:
                rm = -1
            else:
                if (p[i] == player_type and (p[i-4]*p[i]) < 0 and p[i-9] == 0):
                    rm = i - 9
                else:
                    rm = -1
        return [lm, rm]
    
    # Returns a list of all posible reverse jump moves of the form; [[0, [lm, rm]], [1, [lm, rm]]]
    # Takes in variables p, which is the board vector, indx, which is the index of the piece to be moved,
    # and type which is the player type.
    def findJumpsReverse(self, p, player_type):
        moves = []
        for i in range(32):
            m_arr = self.findJumpsReverseSinglePiece(p, i, player_type)
            moves.append([i, m_arr])
        return moves
    
    # variable "type" is an integer denoting the type of piece. 2 White -2 Black
    # variable "p" is an array of the current board positions
    def findKingMoves(self, p, player_type):
        arr1 = self.findSingleMoves(p, player_type)
        arr2 = self.findSingleMovesReverse(p, player_type)
        moves = []
        for i in range(32):
            temp = []
            temp.extend(arr1[i][1])
            temp.extend(arr2[i][1])
            moves.append([i, temp])
        return moves

    # Returns an array of all moves that all King pieces can jump to.
    # Takes in variables p, which is the board vector, and type which is the player type.
    def findKingJumps(self, p, type):
        arr1 = self.findJumps(p, type)
        arr2 = self.findJumpsReverse(p, type)
        moves = []
        for i in range(32):
            temp = []
            temp.extend(arr1[i][1])
            temp.extend(arr2[i][1])
            moves.append([i, temp])
        return moves

    # Returns an array of the positions that a single King piece can jump to.
    # Takes in variables p, which is the board vector, indx, which is the index of the piece to be moved,
    # and type which is the player type.
    def findKingJumpsSinglePiece(self, p, indx, type):
        arr = self.findJumpsSinglePiece(p, indx, type) + self.findJumpsReverseSinglePiece(p, indx, type)
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == -1:
                arr.pop(i)
        return arr

    # Removes the -1 values from the array of moves provided and then returns it.
    def removeNoMove(self, arr):
        moves = []
        for i in arr:
            temp = []
            for j in i[1]:
                if j >= 0:
                    temp.append(j)
            if temp != []:
                moves.append([i[0],temp])
        return moves

    # Returns a random move for the random player.
    # Takes in arr of possible jumps.
    def selectRandomMove(self, arr):
        rng1 = random.randrange(0, len(arr))
        rng2 = random.randrange(0, len(arr[rng1][1]))
        return [arr[rng1][0], arr[rng1][1][rng2]]

    # Returns a random jump move for the inner jumps of the random player.
    # Takes in arr of possible jumps.
    def selectRandomInnerJump(self, arr):
        rng1 = random.randrange(0, len(arr[1]))
        return [arr[0], arr[1][rng1]]
    
    # Removes inner brackets from array move.
    def cleanSelectedMove(self, arr):
        return [arr[0], arr[1][0]]

    # Takes in array of moves with format [[1, [2]], [3, [4, 5]]] and returns an array with format [[1, 2], [3, 4], [3, 5]].
    def cleanArrayMoves(self, arr):
        output_arr = []
        for i in range(len(arr)):
            for j in range(len(arr[i][1])):
                output_arr.append([arr[i][0], arr[i][1][j]])
        return output_arr

    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    # Variable p is vector representing the checkers board.
    def movePieceNN(self, p, sm):
        temp = self.__checkForKingNN(p, sm)
        test = sm[0] - sm[1]
        if (test > 0):
            if (test == 7):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] - 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] - 3] = 0
            elif (test == 9):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] - 5] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] - 4] = 0
        else:
            if (test == -7):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] + 3] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] + 4] = 0
            elif (test == -9):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] + 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] + 5] = 0
        p[sm[0]] = 0
        p[sm[1]] = temp

    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def movePiece(self, sm):
        temp = self.__checkForKing(sm)
        test = sm[0] - sm[1]
        if(test > 0):
            if(test == 7):
                if(0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0]-4] = 0
                elif(4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0]-3] = 0
            elif(test == 9):
                if(0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0]-5] = 0
                elif(4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0]-4] = 0
        else:
            if(test == -7):
                if(0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0]+3] = 0
                elif(4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0]+4] = 0
            elif(test == -9):
                if(0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0]+4] = 0
                elif(4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0]+5] = 0
        self.board_vector[sm[0]] = 0
        self.board_vector[sm[1]] = temp

    # Removes -1 from list.  Takes in [9, -1] and returns [9] or takes in [1, 2] and returns [1, 2].
    # Used in conjunction with findJumpsSinglePiece() function.
    def removeNegatives(self, arr):
        temp = []
        for i in range(len(arr)):
            if arr[i] != -1:
                temp.append(arr[i])
        return temp

    # Calculates all jump possibilities from given jump for a single piece.  Returns list of branching jumps.
    def calculateJumpPaths(self, jump, boardCopy):
        self.movePieceNN(boardCopy, jump)
        type = boardCopy[jump[1]]
        # print("move made -", jump)
        # print("type -", boardCopy[jump[1]])
        if type == 1:
            njs = self.removeNegatives(self.findJumpsSinglePiece(boardCopy, jump[1], type))
        elif type == -1:
            njs = self.removeNegatives(self.findJumpsReverseSinglePiece(boardCopy, jump[1], type))
        else:
            njs = self.findKingJumpsSinglePiece(boardCopy, jump[1], type)
        # print("njs -", njs)

        temp = []
        if len(njs) == 0:
            temp.append(jump)
        elif len(njs) == 1:
            # print("len 1", njs, "jump", jump)
            nextJump = [jump[1], njs[0]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy))
        elif len(njs) == 2:
            # print("len 2", njs, "jump", jump)
            nextJump = [jump[1], njs[0]]
            nextJump2 = [jump[1], njs[1]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump2, boardCopy[:]))
        else:
            # print("len 3", njs)
            nextJump = [jump[1], njs[0]]
            nextJump2 = [jump[1], njs[1]]
            nextJump3 = [jump[1], njs[2]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump2, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump3, boardCopy[:]))
        return temp

    # Returns an array of all possible jump paths from given array input.
    # Input is an array of jumps that can be made following the first.
    # Input comes from calculateJumpPaths() function output.
    def createJumpPathsBuilder(self, arr):
        narr = self.flattenJumpPathArray(arr)
        output = []
        narr_copy = narr[:]

        pathEnds = []
        for i in range(1, len(narr_copy) - 1):
            if narr_copy[i][1] != narr_copy[i + 1][0] or (
                    narr_copy[i][1] == narr_copy[i + 1][0] and narr_copy[i][0] == narr_copy[i + 1][1]):
                pathEnds.append(i)
        pathEnds.append(len(narr_copy) - 1)
        pathE = pathEnds[::-1]

        for i in range(len(pathE)):
            output.append([])

        for i in range(len(output)):
            # print("\npath")
            temp = narr_copy[pathE[i]][:]
            output[i].append(temp)
            for j in range(pathE[i] - 1, -1, -1):
                # print("temp", temp, "next", narr_copy[i])
                if temp[0] == narr_copy[j][1] and temp[1] == narr_copy[j][0]:
                    continue
                elif temp[0] == narr_copy[j][1]:
                    # print("appended", narr_copy[i], "to", path)
                    output[i].append(narr_copy[j][:])
                    temp = narr_copy[j][:]

        for i in range(len(output)):
            output[i] = output[i][::-1]
        return output

    # Takes an array of arrays as input and returns a flattened array. Works within createJumpPathsBuilder() function.
    # Ex: [[3, 10], [[10, 17]], [[10, 19]]] -> [[3, 10], [10, 17], [10, 19]]
    def flattenJumpPathArray(self, arr):
        output = []
        if isinstance(arr[0], int):
            return [arr]
        for jump in arr:
            if isinstance(jump[0], int):
                output.append(jump)
            else:
                for nJump in jump:
                    output.extend(self.flattenJumpPathArray(nJump))
        return output

    # Determine if a piece needs to be Kinged
    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def __checkForKing(self, sm):
        if(self.board_vector[sm[0]] == 1):
            if(28 <= sm[1] < 32):
                return 2
            else:
                return 1
        elif(self.board_vector[sm[0]] == -1):
            if(0 <= sm[1] < 4):
                return -2
            else:
                return -1
        else:
            return self.board_vector[sm[0]]

    # Determine if a piece needs to be Kinged.  Works in movePieceNN in CalculateJumpsPaths due to boardCopies.
    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def __checkForKingNN(self, p, sm):
        if (p[sm[0]] == 1):
            if (28 <= sm[1] < 32):
                return 2
            else:
                return 1
        elif (p[sm[0]] == -1):
            if (0 <= sm[1] < 4):
                return -2
            else:
                return -1
        else:
            return p[sm[0]]
    
    # returns array [w, b] containing w: number of white pieces, b: number of black pieces on the board.
    def __countPieces(self):
        b = 0
        w = 0
        for i in self.board_vector:
            if(i == 1 or i == 2): w += 1
            elif(i == -1 or i == -2): b += 1
        return [w, b]
    
    # Returns the index of the maximum value within a given array a.  Array must contain number values.
    @staticmethod
    def indxOfMax(a):
        if(len(a) == 0):
            print("array empty")
        else:
            indx = 0
            max = 0
            for i in range(len(a)):
                if(a[i] > max):
                    max = a[i]
                    indx = i
            return indx

    # Checks the game board to determine if a player has won.  Based on amount of pieces remaining.
    # Returns 'w' when the white player wins and 'b' when the black player wins.
    def __checkVictory(self):
        wb = self.__countPieces()
        if wb[0] == 0:
            # print("Black Victory.  All Pieces Taken.")
            return 'b'
        elif wb[1] == 0:
            # print("White Victory.  All Pieces Taken.")
            return 'w'
    
    # Variable boolean either True or False to show game board.
    def game(self, boolean):
        if boolean:
            self.showBoard()
            print("\n")
        c = 0
        while(c < 100):
            c += 1
            if(c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boolean:  # info on possible moves
                    print("\nall moves -",am)
                    print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if(boolean):
                        print("selected move", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boolean:  # info on possible moves
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                    while(jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boolean:  # info on possible moves
                                    print("selected move", selMove)
                        if(jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boolean:  # info on possible moves
                    print("\nall moves -",am)
                    print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if(boolean):
                        print("selected move", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boolean:  # info on possible moves
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                    while(jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove =  self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boolean:  # info on possible moves
                                    print("selected move", selMove)
                        if(jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
            if(boolean):
                print("iteration:", c)
                self.showBoard()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"
    
    # Variable boolean either True or False to show game board.
    def gameTest(self, boolean):
        print("Game Start")
        #board_vector[14] = 1; board_vector[18] = -1; board_vector[19] = -1; board_vector[25] = -1; board_vector[20] = 1
        self.showBoardV2()
        print("\n")
        c = 0
        while(c < 100):
            c += 1
            if(c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                print("\nall moves -",am)
                print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                    while(jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove =  self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                print("selected move", selMove)
                        if(jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                print("\nall moves -",am)
                print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                    while(jm != []):
                        tp1 = jm
                        print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove =  self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                print("selected move", selMove)
                        if(jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
            print("iteration:", c)
            self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"
    
    # Test for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Random moves are Black.
    def gameTestNN_White(self, bool,  nn):
        if bool:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        testerNN = nn
        c = 0
        while(c < 100):
            c += 1
            if(c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
    
                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -",am)
                    print("all jumps -",jm)
                if(jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif(jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -",am)
                    print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if bool:
                        print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if bool:
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                    while(jm != []):
                        tp1 = jm
                        if bool:
                            print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if bool:
                                    print("selected move", selMove)
                        if jm == tp1:
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(self.findKingJumps(self.board_vector, -2))
            if bool:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Test for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is Black. Random moves are White.
    def gameTestNN_Black(self, boole, nn):
        if boole:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boole:
                    print("\nall moves -",am)
                    print("all jumps -",jm,"\n")
                if(jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif(jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if boole:
                        print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boole:
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                    while(jm != []):
                        tp1 = jm
                        if boole:
                            print("new jumps -", jm)
                        for i in jm:
                            if(i[0] == selMove[1]):
                                selMove =  self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boole:
                                    print("selected move", selMove)
                        if(jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []                
                
                if boole:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if boole:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))
                    
                    maxIndex = self.indxOfMax(movesScores)
                    if boole:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if boole:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))                    
                    if boole:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))
                    
                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if boole:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            if boole:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Test for a single checkers game run with a Neural Network.
    # Variable nn1 and nn2 represents the neural networks being used.
    # Neural Network 1 is White. Neural Network 2 is Black.
    # Variable bool prints out game information if True else is does not if False.
    def gameTestNN(self, bool, nn1, nn2):
        if bool:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(nn1.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(nn1.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(nn2.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(nn2.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            if bool:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Plays a number of n games.
    # Variable n is an integer for number of games to be played. Variable boolean either True or False to show game board.
    def run(self, n, boolean):
        wv = 0
        bv = 0
        draw = 0
        start = time.time()
        for i in range(1, n+1):
            if (i/n*100) % 5 == 0:
                print(str(int(i/n*100)) + "% ", end='', flush=True)
            if i == n:
                print('\n')
            winner = self.game(boolean)
            if (winner == 'w'):
                wv += 1
            elif (winner == 'b'):
                bv += 1
            elif (winner == 'd'):
                draw += 1
        end = time.time()
        print("_____",n,"games played _____")
        print("\nTime taken: %.2f seconds." % (end - start))
        print("White won", wv, "times. = %.2f" % (wv/n*100), "%")
        print("Black won", bv, "times. = %.2f" % (bv/n*100), "%")
        print("Draw", draw, "times. = %.2f" % (draw/n*100), "%")

    # Game for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Player moves are Black.
    def playGameAsBlack(self, bool, nn):
        print("Game Start")
        self.showBoardV2()
        print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                print("White's Turn.")
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                    print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                    print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                print("Black's Turn.")
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    print("White Victory. Black can't move.")
                    return 'w'
                else:
                    tmove = input("Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                    move = tmove.split(" ")
                    move[0] = int(move[0])
                    move[1] = int(move[1])
                    self.movePiece(move)
                    while input("Is there a jump?") == "y":
                        tmove = input("Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                        move = tmove.split(" ")
                        move[0] = int(move[0])
                        move[1] = int(move[1])
                        self.movePiece(move)
            self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Game for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Player moves are Black.
    def playGameAsWhite(self, bool, nn):
        print("Game Start")
        self.showBoardV3()
        print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                print("White's Turn.")
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("Black Victory. White can't move.")
                    return 'b'
                else:
                    if jm != []:
                        print("Jump available!")
                    self.showBoardIndices()
                    tmove = input("Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                    move = tmove.split(" ")
                    move[0] = int(move[0])
                    move[1] = int(move[1])
                    while True:
                        if [move[0], move[1]] in self.cleanArrayMoves(am) or [move[0], move[1]] in self.cleanArrayMoves(jm):                            
                            self.movePiece(move)
                            break
                        else:
                            print("\nMove not possible.")  
                            tmove = input("Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                            move = tmove.split(" ")
                            move[0] = int(move[0])
                            move[1] = int(move[1])
                    
                    if jm != []:
                        while input("Is there another jump?") == "y":
                            tmove = input("Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                            move = tmove.split(" ")
                            move[0] = int(move[0])
                            move[1] = int(move[1])
                            self.movePiece(move)
            else:
                print("Black's Turn.")
                time.sleep(3)
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                    print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                    print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            time.sleep(1)
            self.showBoardV3()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    def liveGameRunner(self):
        result = 0
        play_as = input("Black or white?\n>> ")
        if play_as == "black":
            result = self.playGameAsBlack(False, self.whiteNN)
        elif play_as == "white":
            result = self.playGameAsWhite(False, self.blackNN)
            
        if result == "w":
            print("***** White Wins!! *****")
        elif result == "b":
            print("***** Black Wins!! *****")


####################################################################################
# GUI Functions

    def hasJump(self, index):
        jump = 0
        if self.board_vector[index] == 2 or self.board_vector[index] == -2:
            jump = self.findKingJumpsSinglePiece(self.board_vector, index, self.board_vector[index])
        else:
            if self.board_vector[index] == 1:
                jump = self.findJumpsSinglePiece(self.board_vector, index, self.board_vector[index])
            elif self.board_vector[index] == -1:
                jump = self.findJumpsReverseSinglePiece(self.board_vector, index, self.board_vector[index])
            else:
                return "error"
        jump = self.removeNegatives(jump)
        #print("move =", jump)
        return len(jump) != 0

    def set_gui_player(self, player):
        self.gui_player = player

    def gui_check(self, c, move):
        if self.gui_player == "White":
            if (c%2) == 1:
                return self.gui_playGameAsWhite_Player(move)           # Takes in move to be made.
            else:
                return self.gui_playGameAsWhite_Opponant()             # Returns move to be made.
        elif self.gui_player == "Red":
            if (c%2) == 0:
                return self.gui_playGameAsBlack_Player(move)           # Takes in move to be made.
            else:
                return self.gui_playGameAsBlack_Opponant()
        else:
            print("Player Error. Incorrect Player type.")

    # runs check on move passed to it. Playing as the Red/Black player.
    def gui_playGameAsBlack_Player(self, move):
        moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
        jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps
        if (jm == [] and am == []):
            return 'b'
        else:
            if move in self.cleanArrayMoves(am) or move in self.cleanArrayMoves(jm):
                if move in self.cleanArrayMoves(am) and jm != []:
                    return [False, False]
                else:
                    self.movePiece(move)
                #print("In Brain.  Making Move.", move)
                if self.hasJump(move[1]):
                    return [True, True]
                else:
                    return [True, False]
            else:
                return [False, False]

    # Returns the move to be made by the opponant. Playing as the Red/Black player.
    def gui_playGameAsBlack_Opponant(self):
        testerNN = self.whiteNN
        time.sleep(2)

        moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
        jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps

        movesScores = []
        movesScoresJumps = []

        if (jm == [] and am == []):
            return 'b'
        elif (jm == []):
            cleanedAM = self.cleanArrayMoves(am)
            for i in range(len(cleanedAM)):
                boardCopy = self.board_vector[:]
                self.movePieceNN(boardCopy, cleanedAM[i])
                movesScores.append(testerNN.feedForward(boardCopy))

            maxIndex = self.indxOfMax(movesScores)
            self.movePiece(cleanedAM[maxIndex])
            return cleanedAM[maxIndex]
        else:
            cleanedJM = self.cleanArrayMoves(jm)
            allJumps = []
            for i in range(len(cleanedJM)):
                tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                allJumps.extend(self.createJumpPathsBuilder(tempjm))
            for path in allJumps:
                boardCopy = self.board_vector[:]
                for jump in path:
                    self.movePieceNN(boardCopy, jump)
                movesScoresJumps.append(testerNN.feedForward(boardCopy))

            maxIndex = self.indxOfMax(movesScoresJumps)
            for jump in allJumps[maxIndex]:
                self.movePieceNN(self.board_vector, jump)
            return allJumps[maxIndex]

    # runs check on move passed to it. Playing as the White player.
    def gui_playGameAsWhite_Player(self, move):
        moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
        jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps
        if (jm == [] and am == []):
            return 'b'
        else:
            if move in self.cleanArrayMoves(am) or move in self.cleanArrayMoves(jm):
                if move in self.cleanArrayMoves(am) and jm != []:
                    return [False, False]
                else:
                    self.movePiece(move)
                #print("In Brain.  Making Move.", move)
                if self.hasJump(move[1]):
                    return [True, True]
                else:
                    return [True, False]
            else:
                return [False, False]

    # Returns the move to be made by the opponant. Playing as the White player.
    def gui_playGameAsWhite_Opponant(self):
        testerNN = self.blackNN
        time.sleep(2)

        moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
        jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps

        movesScores = []
        movesScoresJumps = []

        if (jm == [] and am == []):
            return 'w'
        elif (jm == []):
            cleanedAM = self.cleanArrayMoves(am)
            for i in range(len(cleanedAM)):
                boardCopy = self.board_vector[:]
                self.movePieceNN(boardCopy, cleanedAM[i])
                movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

            maxIndex = self.indxOfMax(movesScores)
            self.movePiece(cleanedAM[maxIndex])
            return cleanedAM[maxIndex]
        else:
            cleanedJM = self.cleanArrayMoves(jm)
            allJumps = []
            for i in range(len(cleanedJM)):
                tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                allJumps.extend(self.createJumpPathsBuilder(tempjm))
            for path in allJumps:
                boardCopy = self.board_vector[:]
                for jump in path:
                    self.movePieceNN(boardCopy, jump)
                movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

            maxIndex = self.indxOfMax(movesScoresJumps)
            for jump in allJumps[maxIndex]:
                self.movePieceNN(self.board_vector, jump)
            return allJumps[maxIndex]

    # Test to see whether there is a victor.
    # Variable c is the turn counter.
    # Returns end result or false if game is not over.
    def gui_Victory_Check(self, c):
        tester = self.__checkVictory()
        if tester == 'w':
            return 'w'
        elif tester == 'b':
            return 'b'
        elif c == 100:
            return "d"
        else:
            return False
