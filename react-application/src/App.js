import React from "react";
import Footer  from "./components/Footer"
import Header from "./components/Header";
import Items from "./components/Items";
import './index.css';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [
                {
                    "id": 1,
                    "fileName": "Thesis_Chapter1",
                    "fileSize": "2MB",
                    "fileExtension": "docx",
                    "pageCount": 30,
                    "printType": "black-and-white",
                    "orderStatus": "pending",
                    "printPrice": "150",
                    "orderCreationDate": "2024-04-20",
                    "orderCompletionDate": "2024-04-22"
                },
                {
                    "id": 2,
                    "fileName": "Project_Presentation",
                    "fileSize": "5MB",
                    "fileExtension": "ppt",
                    "pageCount": 15,
                    "printType": "color",
                    "orderStatus": "printed",
                    "printPrice": "225",
                    "orderCreationDate": "2024-04-18",
                    "orderCompletionDate": "2024-04-19"
                },
                {
                    "id": 3,
                    "fileName": "Annual_Report_2023",
                    "fileSize": "8MB",
                    "fileExtension": "pdf",
                    "pageCount": 50,
                    "printType": "color",
                    "orderStatus": "in queue",
                    "printPrice": "500",
                    "orderCreationDate": "2024-04-21",
                    "orderCompletionDate": "2024-04-23"
                },
                {
                    "id": 4,
                    "fileName": "Annual_Report_2023",
                    "fileSize": "8MB",
                    "fileExtension": "pdf",
                    "pageCount": 50,
                    "printType": "color",
                    "orderStatus": "in queue",
                    "printPrice": "500",
                    "orderCreationDate": "2024-04-21",
                    "orderCompletionDate": "2024-04-23"
                },
                {
                    "id": 5,
                    "fileName": "Annual_Report_2023",
                    "fileSize": "8MB",
                    "fileExtension": "pdf",
                    "pageCount": 50,
                    "printType": "color",
                    "orderStatus": "in queue",
                    "printPrice": "500",
                    "orderCreationDate": "2024-04-21",
                    "orderCompletionDate": "2024-04-23"
                }
            ]
        }
    }
    render() {
        return (
            <div className="wrapper">
                <Header/>
                <Items items={this.state.items}/>
                <Footer/>
            </div>
        );
    }
}

export default App;