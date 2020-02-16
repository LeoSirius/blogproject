import React from 'react';

import Node from './node';
import Leaf from './leaf';

import internalAPI from './internal-api';

import tree from './summary';

import './css/app.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tree: tree,
    }
  }

  componentDidMount() {
    internalAPI.getDocTree().then(res => {
      console.log(res.data.doctree)
      this.setState({tree: res.data.doctree.children})
    }).catch(err => {

    });
  }

  renderTree() {
    let { tree } = this.state;
    return tree.map(node => {
      if (node.hasOwnProperty('children')) {
        return (
          <Node node={node}/>
        );
      } else {
        return (
          <Leaf leaf={node}/>
        )
      }
    })
  }

  render() {
    return (
      <div>
        <div className="top-bar"></div>
        <div className="main-content">
          <div className="column tree">
            {this.renderTree()}
          </div>
          <div className="column doc">dovdoc</div>
          <div className="column nav-bar">navbariii</div>
        </div>
        <div className="footer"></div>
      </div>
    )
  }
}





export default App;