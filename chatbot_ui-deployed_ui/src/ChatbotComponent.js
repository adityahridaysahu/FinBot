// import React from "react";
// import ActionProvider from "./ActionProvider";

// class ChatbotComponent extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       messages: [],
//     };
//     this.actionProvider = new ActionProvider(this.createChatBotMessage, this.setState.bind(this));
//   }

//   createChatBotMessage = (content) => {
//     return {
//       id: new Date().getTime(),
//       content,
//     };
//   };

//   componentDidMount() {
//     this.actionProvider.startTimeout();
//   }

//   handleOptionSelect = (optionValue) => {
//     this.actionProvider.handleOptionSelect(optionValue);
//   };

//   renderOptions = (message) => {
//     return (
//       <div key={message.id} className="options-message">
//         {message.content}
//       </div>
//     );
//   };

//   renderBotMessage = (message) => {
//     return (
//       <div key={message.id} className="bot-message">
//         {message.content}
//       </div>
//     );
//   };

//   render() {
//     return (
//       <div>
//         {this.state.messages.map((message) => {
//           if (message.type === "options") {
//             return this.renderOptions(message);
//           } else {
//             return this.renderBotMessage(message);
//           }
//         })}
//       </div>
//     );
//   }
// }

// export default ChatbotComponent;
