pragma solidity ^0.5.1;

contract CoinFlip {

    uint constant public BET_MIN        = 1 wei;    // The minimum bet
    uint constant public HOUSE_PCT = 10;
    uint public initialBet;                            // Bet of first player


    // Players' addresses
    address payable playerA;
    address payable HouseWallet = 0x10b21F7DC7d6BDB16660D827442c7edb3d2523eA; //


    

    /**************************************************************************/
    /*************************** REGISTRATION PHASE ***************************/
    /**************************************************************************/



    // Register a player.
    // Return player's ID upon successful registration.

    modifier validBet() {
        require(msg.value >= BET_MIN);
        require(initialBet == 0 || msg.value >= initialBet);
        _;
    }


    function register() public payable validBet returns (uint) {
        if (playerA == address(0x0)) {
            playerA    = msg.sender;
            initialBet = msg.value;
            return 1;
        } else {
            return 0;
        }
        
    }

    /**************************************************************************/
    /****************************** RESULT PHASE ******************************/
    /**************************************************************************/



    // Compute the outcome and pay the winner(s).


    function getOutcome() public returns (uint) {    

        address payable addrA = playerA;
        address payable addrC = HouseWallet;

        uint betPlayerA       = initialBet;
        

        reset();  // Reset game before paying to avoid reentrancy attacks
        pay(addrC, HOUSE_PCT);
        uint outcome = 1;

        return outcome;
    }

    // Pay the winner(s).
    
    function pay(address payable addrC, uint house_fee) private {
    
        // Uncomment lines below if you need to adjust the gas limit
      
            addrC.transfer(address(this).balance);
           
    }

    // Reset the game.
    function reset() private {
        initialBet      = 0;
        playerA         = address(0x0);
            
    }

    /**************************************************************************/
    /**************************** HELPER FUNCTIONS ****************************/
    /**************************************************************************/

    // Return contract balance
    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Return player's ID
    function whoAmI() public view returns (uint) {
        if (msg.sender == playerA) {
            return 1;
        } else {
            return 0;
        }
    }
}


