import React from 'react';
import tree from './summary';

import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tree: tree,
    }
  }

  componentDidMount() {
    // this.setState({tree: tree})
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
    return this.renderTree();
  }
}

class Node extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isDisplayChildren: false,
    }
  }

  toggleDisplayChildren = (e) => {
    e.stopPropagation();
    this.setState({isDisplayChildren: !this.state.isDisplayChildren});
  }

  render() {
    let { node } = this.props;
    let { isDisplayChildren } = this.state;
    console.log(isDisplayChildren)
    return (
      <div className='node' onClick={this.toggleDisplayChildren}>
        {node.name}
        <div className={ isDisplayChildren ? '' :  'display-none'}>
        {node.children.map((node, index) => {
          if (node.hasOwnProperty('children')) {
            return (
              <Node key={node.name} node={node}/>
            )
          } else {
            return (
              <Leaf key={node.name} leaf={node}/>
            )
          }
        })}
        </div>
      </div>
    );
  }
}

class Leaf extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  tmp = (e) => {
    e.stopPropagation();
  }

  render() {
    let { leaf } = this.props;
    return (
      <div className='leaf' onClick={this.tmp}>
        {leaf.name}
      </div>
    );
  }
}

export default App;