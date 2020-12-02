import React from "react";

class SetString extends React.Component {
    state = { stackId: null };

    constructor(props) {
        super(props);
        this.state = {
            result: 0,
            callval: 0,
            callnum: 0,
            min: 1,
            max: 6,
            number1: 1,
            number2: 1,
            number3: 1,
            number4: 1,
            number5: 1,
            number6: 1,
            number7: 1,
            number8: 1,
            number9: 1,
            number10: 1,
            number11: 1,
            number12: 1,
            number13: 1,
            number14: 1,
            number15: 1,
            number16: 1,
            number17: 1,
            number18: 1,
            number19: 1,
            number20: 1,
        }
    }

    componentDidMount() {
        this.setState({ number1: this.generateNumber(this.state.min, this.state.max),
            number2: this.generateNumber(this.state.min, this.state.max),
            number3: this.generateNumber(this.state.min, this.state.max),
            number4: this.generateNumber(this.state.min, this.state.max),
            number5: this.generateNumber(this.state.min, this.state.max),
            number6: this.generateNumber(this.state.min, this.state.max),
            number7: this.generateNumber(this.state.min, this.state.max),
            number8: this.generateNumber(this.state.min, this.state.max),
            number9: this.generateNumber(this.state.min, this.state.max),
            number10: this.generateNumber(this.state.min, this.state.max),
            number11: this.generateNumber(this.state.min, this.state.max),
            number12: this.generateNumber(this.state.min, this.state.max),
            number13: this.generateNumber(this.state.min, this.state.max),
            number14: this.generateNumber(this.state.min, this.state.max),
            number15: this.generateNumber(this.state.min, this.state.max),
            number16: this.generateNumber(this.state.min, this.state.max),
            number17: this.generateNumber(this.state.min, this.state.max),
            number18: this.generateNumber(this.state.min, this.state.max),
            number19: this.generateNumber(this.state.min, this.state.max),
            number20: this.generateNumber(this.state.min, this.state.max)
        })     
    }  

    callBid = () => {
        const dieNum = [this.number1, this.number2, this.number3, this.number4, this.number5, this.number6, this.number7,this.number8, this.number9, this.number10, this.number11, this.number12, this.number13, this.number14, this.number15, this.number16, this.number17, this.number18, this.number19, this.number20];
        
        var verify=0;
        for(const [i, value] of dieNum.entries())
        {
            if (dieNum[{i}] === this.callval)
            {
                verify=verify+1;
                console.log(this.callval);
            }
        }
        if(verify>=this.callnum)
        {
            this.setState({ result: true })
            alert("Unsuccessful")
        }
        else
        {
            this.setState({ result: false })
            alert("Successful")
        }
        
    }
    
    generateNumber = (min, max) => {
      return Math.floor(Math.random()*(max-min+1)+min)
    }

    numChange = (event) => {
        this.setState({ callnum: event.target.value})
        console.log(this.callnum)
    }
      
    valChange = (event) => {
      this.setState({ callval: event.target.value})
      console.log(this.callval)
    }
    
    getInputs = () => {
      if(this.state.min > this.state.max ){
        const minTemp = this.state.min
        const maxTemp = this.state.max
        this.setState(
        { 
          min: maxTemp,
          max: minTemp
        }, () =>
          this.setState({
            number1: this.generateNumber(this.state.min, this.state.max),
            number2: this.generateNumber(this.state.min, this.state.max),
            number3: this.generateNumber(this.state.min, this.state.max),
            number4: this.generateNumber(this.state.min, this.state.max),
            number5: this.generateNumber(this.state.min, this.state.max),
            number6: this.generateNumber(this.state.min, this.state.max),
            number7: this.generateNumber(this.state.min, this.state.max),
            number8: this.generateNumber(this.state.min, this.state.max),
            number9: this.generateNumber(this.state.min, this.state.max),
            number10: this.generateNumber(this.state.min, this.state.max),
            number11: this.generateNumber(this.state.min, this.state.max),
            number12: this.generateNumber(this.state.min, this.state.max),
            number13: this.generateNumber(this.state.min, this.state.max),
            number14: this.generateNumber(this.state.min, this.state.max),
            number15: this.generateNumber(this.state.min, this.state.max),
            number16: this.generateNumber(this.state.min, this.state.max),
            number17: this.generateNumber(this.state.min, this.state.max),
            number18: this.generateNumber(this.state.min, this.state.max),
            number19: this.generateNumber(this.state.min, this.state.max),
            number20: this.generateNumber(this.state.min, this.state.max)
          })
        );
      } else {
        this.setState({
            number1: this.generateNumber(this.state.min, this.state.max),
            number2: this.generateNumber(this.state.min, this.state.max),
            number3: this.generateNumber(this.state.min, this.state.max),
            number4: this.generateNumber(this.state.min, this.state.max),
            number5: this.generateNumber(this.state.min, this.state.max),
            number6: this.generateNumber(this.state.min, this.state.max),
            number7: this.generateNumber(this.state.min, this.state.max),
            number8: this.generateNumber(this.state.min, this.state.max),
            number9: this.generateNumber(this.state.min, this.state.max),
            number10: this.generateNumber(this.state.min, this.state.max),
            number11: this.generateNumber(this.state.min, this.state.max),
            number12: this.generateNumber(this.state.min, this.state.max),
            number13: this.generateNumber(this.state.min, this.state.max),
            number14: this.generateNumber(this.state.min, this.state.max),
            number15: this.generateNumber(this.state.min, this.state.max),
            number16: this.generateNumber(this.state.min, this.state.max),
            number17: this.generateNumber(this.state.min, this.state.max),
            number18: this.generateNumber(this.state.min, this.state.max),
            number19: this.generateNumber(this.state.min, this.state.max),
            number20: this.generateNumber(this.state.min, this.state.max)
        })
      }

    }

    handleKeyDown = e => {
        // if the enter key is pressed, set the value with the string
        if (e.keyCode === 13) {
            this.setValue(e.target.value);
            // this.shuffle();
        }
    };

    setValue = value => {
        const { drizzle, drizzleState } = this.props;
        const contract = drizzle.contracts.MyStringStore;

        // let drizzle know we want to call the `set` method with `value`
        const stackId = contract.methods["set"].cacheSend(value, {
            from: drizzleState.accounts[0]
        });

        // save the `stackId` for later reference
        this.setState({ stackId });
    };

    getTxStatus = () => {
        // get the transaction states from the drizzle state
        const { transactions, transactionStack } = this.props.drizzleState;

        // get the transaction hash using our saved `stackId`
        const txHash = transactionStack[this.state.stackId];

        // if transaction hash does not exist, don't display anything
        if (!txHash) return null;

        // otherwise, return the transaction status
        return `Transaction status: ${transactions[txHash] && transactions[txHash].status}`;
    };

    // render() {
        // return (
        //     <div>
        //         <p>Enter the bid</p>
        //         <input type="text" onKeyDown={this.handleKeyDown} /><br></br><br></br>
        //         <input type="text" onKeyDown={this.handleKeyDown} /><br></br><br></br>
        //         <input type="text" onKeyDown={this.handleKeyDown} /><br></br><br></br>
        //         <input type="text" onKeyDown={this.handleKeyDown} /><br></br><br></br>
        //         <div>{this.getTxStatus()}</div>
        //     </div>
        // );
    // }

    render() {
        return (
          <div id="generator">
            <div id="title">Dice</div>
            <p id="rNum">{ this.state.number1 }, { this.state.number2 }, { this.state.number3 }, { this.state.number4 }, { this.state.number5 }</p>
            <div id="inputContainer">
              <div id="headers"> 
              </div>
              <div id="inputs">
                <input id="generate" type="submit" value="Roll Dice" onClick={ this.getInputs }/>
              </div>
                <br></br>
                <input id="numdie" min={ this.state.callnum } max="20" type="number" value={ this.state.callnum } onChange={this.numChange} />
                <input id="val" min={ this.state.callval } max="6" type="number" value={ this.state.callval } onChange={this.valChange} />
                <br></br>
                <br></br>
                <div id="SubmitBid">
                    <input id="subval" type="submit" value="Submit Bid" onClick={this.setValue} />
                </div>
                <br></br>
                <div id="CallBid">
                    <input id="subcall" type="submit" value="Call Bid" onClick={this.callBid}/>
                </div>
            </div>
          </div>
        );
      }
    }


export default SetString;