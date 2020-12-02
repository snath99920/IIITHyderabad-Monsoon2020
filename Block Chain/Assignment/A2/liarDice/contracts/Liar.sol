pragma solidity >=0.4.22 <0.8.0;

contract Liar {
    // number of dices with each player
    uint256 public no_p1;
    uint256 public no_p2;
    uint256 public no_p3;
    uint256 public no_p4;
    uint[5] p1;
    uint[5] p2;
    uint[5] p3;
    uint[5] p4;

    uint bid_value;
    uint bid_count;

    function roll() public {
        for (uint i=0 ; i<no_p1 ; i++){
           p1[i] = uint(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 6;
           p1[i]++;

        }
        for (uint i=0 ; i<no_p2 ; i++){
           p2[i] = uint(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 6;
           p2[i]++;

        }
        for (uint i=0 ; i<no_p3 ; i++){
           p3[i] = uint(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 6;
           p3[i]++;

        }
        for (uint i=0 ; i<no_p4 ; i++){
           p4[i] = uint(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 6;
           p4[i]++;

        }
    }


    function raise_bid(uint number, uint count) public {
        if(number < bid_value)
        {
            //invalid bid (send message to react)
        }
        else
        {
            if(number==bid_value && count <= bid_count)
            {
                // invalid bid mesaage
            }
            else
            {
                bid_value=number;
                bid_count=count;
            }
        }
    }
    uint t;
    function challenge_bid()  public {
        for (uint i=0; i<no_p1; i++)
        {
            if(p1[i]==bid_value)
            {
                t++;
            }
        }
        for (uint i=0; i<no_p2; i++)
        {
            if(p2[i]==bid_value)
            {
                t++;
            }
        }
        for (uint i=0; i<no_p3; i++)
        {
            if(p3[i]==bid_value)
            {
                t++;
            }
        }
        for (uint i=0; i<no_p4; i++)
        {
            if(p4[i]==bid_value)
            {
                t++;
            }
        }
        if(t>= bid_value)
        {
            //Bid seccessful
        }
        else
        {
            // bid unsuccessful
        }
    }
}

