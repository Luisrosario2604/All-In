### python3 -m robot test_blackJack_decision.robot ###

*** Settings ***
Library      BuiltIn
Library	     blackJack.BlackJack 	0

*** Variables ***

*** Test Cases ***

############## TEST ON CARDS ###############

TEST A A - 2
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		2
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		S

TEST A A 6 - 3
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		S
	${list}=	Create list		moi		6
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		R

TEST A A A - 5
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		S
	${list}=	Create list		moi		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		T

TEST 4 10 - 5
	${list}=	Create list		moi		4
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		5
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		R

TEST 6 10 - 10
	${list}=	Create list		moi		6
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		T

TEST 3 3 - 3
	${list}=	Create list		moi		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		S

TEST 9 9 - A
	${list}=	Create list		moi		9
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		9
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier		1
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		R

TEST 2 3 5 7 - 8
	${list}=	Create list		moi		2
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier 	8
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		T
	${list}=	Create list		moi		5
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		T
	${list}=	Create list		moi		7
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		R

TEST 2 3 4 5 6 2 3 4 10 10 - 5
    ${list}=	Create list		other		2
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		4
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		5
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		6
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		2
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		3
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		other		4
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		moi		10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
	${list}=	Create list		croupier 	5
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		S

TEST 12 13 10 - 10
    ${list}=	Create list		moi		12
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		moi		13
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		${False}
    ${list}=	Create list		croupier   	10
    ${res}= 		blackJack.BlackJack.getCards	${list}
    Should Be Equal	     ${res}		R

################## TEST ON COMPT ####################

TEST 2 3 8 10 11 1
	${list}=	Create list		moi		2
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}
	${list}=	Create list		moi		3
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${2}
	${list}=	Create list		croupier		8
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${2}
	${list}=	Create list		moi		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}
	${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${0}
	${list}=	Create list		croupier		1
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-1}

TEST 10 11 12 10 11 2
	${list}=	Create list		moi		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-1}
	${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-2}
	${list}=	Create list		croupier		12
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-3}
	${list}=	Create list		moi		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-4}
	${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-5}
	${list}=	Create list		croupier		2
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-4}

TEST 2 1 5 5 10 2 10
	${list}=	Create list		moi		2
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}
	${list}=	Create list		other		1
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${0}
	${list}=	Create list		croupier		5
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}
	${list}=	Create list		moi		5
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${2}
	${list}=	Create list		other		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}
	${list}=	Create list		moi		2
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${2}
    ${list}=	Create list		moi		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${1}

TEST 11 12 13 4 12 13 10
	${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-1}
	${list}=	Create list		other		12
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-2}
	${list}=	Create list		croupier		13
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-3}
	${list}=	Create list		moi		4
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-2}
	${list}=	Create list		other		12
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-3}
	${list}=	Create list		moi		13
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-4}
    ${list}=	Create list		moi		10
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-5}

################## SPECIAL TEST ####################

TEST DEALER CARD - 3 5
    ${list}=	Create list		croupier		3
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${3}
    ${list}=	Create list		croupier		5
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${3}

TEST DEALER CARD - 11 13
    ${list}=	Create list		croupier		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${11}
    ${list}=	Create list		croupier		13
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${11}

TEST DEALER CARD - 1 6 13
    ${list}=	Create list		croupier		1
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${1}
    ${list}=	Create list		croupier		6
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${1}
    ${list}=	Create list		croupier		13
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${1}

TEST RESET
    ${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-1}
	${list}=	Create list		other		12
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getLenCards
	Should Be Equal		${res}		${2}
	${list}=	Create list		croupier		13
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getNbCard
	Should Be Equal		${res}		${3}
	${list}=	Create list		moi		4
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getLenPlayer
	Should Be Equal		${res}		${2}
    blackJack.BlackJack.reset
    ${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-2}
    ${res}=		blackJack.BlackJack.getLenCards
	Should Be Equal		${res}		${4}
    ${res}=		blackJack.BlackJack.getNbCard
	Should Be Equal		${res}		${4}
    ${res}=		blackJack.BlackJack.getLenPlayer
	Should Be Equal		${res}		${0}
    ${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${0}
    ${list}=	Create list		moi		1
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${-3}
    ${list}=	Create list		moi		11
    blackJack.BlackJack.getCards	${list}
	${res}=		blackJack.BlackJack.getLenPlayer
	Should Be Equal		${res}		${2}
    blackJack.BlackJack.fullReset
    ${res}=		blackJack.BlackJack.getRealCompt
	Should Be Equal		${res}		${0}
    ${res}=		blackJack.BlackJack.getLenCards
	Should Be Equal		${res}		${0}
    ${res}=		blackJack.BlackJack.getNbCard
	Should Be Equal		${res}		${0}
    ${res}=		blackJack.BlackJack.getLenPlayer
	Should Be Equal		${res}		${0}
    ${res}=		blackJack.BlackJack.getDealerCard
	Should Be Equal		${res}		${0}

################## TEST REAL COMPT ####################

TEST CUMPOND - 1
    LOOP FOR CUMPOND  30  1
TEST CUMPOND - 2
    LOOP FOR CUMPOND  96  2
TEST CUMPOND - 3
    LOOP FOR CUMPOND  111  3
TEST CUMPOND - 4
    LOOP FOR CUMPOND  166  4
TEST CUMPOND - 5
    LOOP FOR CUMPOND  260  5
TEST CUMPOND - 6
    LOOP FOR CUMPOND  261  6
    blackJack.BlackJack.fullReset
    ${res}=		blackJack.BlackJack.getLenCards
	Should Be Equal		${res}		${0}

TEST REAL COMPT - -30
    LOOP FOR REAL COMPT     30      -30     1
TEST REAL COMPT - +48
    LOOP FOR REAL COMPT     96      48     5
TEST REAL COMPT - -35
    LOOP FOR REAL COMPT     111      -37     13
TEST REAL COMPT - +41
    LOOP FOR REAL COMPT     166      41     6
TEST REAL COMPT - -52
    LOOP FOR REAL COMPT     260      -52     11
TEST REAL COMPT - +43
    LOOP FOR REAL COMPT     261      43     2

*** Keywords ***
LOOP FOR CUMPOND
    [Arguments]   ${index}=0    ${expected}=0
	:FOR	${i}	IN RANGE	0	${index}
	\   ${list}=	Create list		moi		13
    \   blackJack.BlackJack.getCards	${list}
    ${NB}=      blackJack.BlackJack.getNbCard
    Log     ${NB}
    ${res}=     blackJack.BlackJack.getCumPond
    Should Be Equal		${res}		${${expected}}

LOOP FOR REAL COMPT
    [Arguments]   ${index}=0    ${expected}=0   ${cards}=1
	:FOR	${i}	IN RANGE	0	${index}
	\   ${list}=	Create list		moi		${cards}
    \   blackJack.BlackJack.getCards	${list}
    ${NB}=      blackJack.BlackJack.getNbCard
    Log     ${NB}
    ${res}=     blackJack.BlackJack.getRealCompt
    Should Be Equal		${res}		${${expected}}