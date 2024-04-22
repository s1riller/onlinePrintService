import React, { Component } from 'react';
import defaultPlaceholder from '../img/default-placeholder.png';


export class Item extends Component {
    state = {
        showDetails: false
    };

    toggleDetails = () => {
        console.log("Toggling details for:", this.props.item.id); // Логирование ID
        this.setState(prevState => ({
            showDetails: !prevState.showDetails
        }));
    }
    render() {
        const { showDetails } = this.state;
        const { item } = this.props;
        return (
            <div className='item'>
                <img src={item.imageUrl || defaultPlaceholder} alt="Print Item Preview" />
                <h2>{item.fileName}</h2>
                <button onClick={this.toggleDetails} className="details-button">
                    {showDetails ? 'Hide Details' : 'Show Details'}
                </button>
                {showDetails && (
                    <div>
                        <h2>{item.orderStatus}</h2>
                        <p>{item.pageCount} pages</p>
                        <p>Type: {item.printType}</p>
                        <b>{item.printPrice}₽</b>
                        <p>Ordered on: {item.orderCreationDate}</p>
                        <p>Ready by: {item.orderCompletionDate}</p>
                        <div className="print-document-again">↻</div>
                    </div>
                )}
            </div>
        );
    }
}

export default Item;
