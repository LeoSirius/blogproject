import React from 'react';

import Node from './node';
import Leaf from './leaf';


class LeftTree extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  leafNodeClicked = (leafNode) => {
    console.log('in tree leaNode = ')
    console.log(leafNode)
    this.props.leafNodeClicked(leafNode);
  }

  renderTree() {
    let { tree } = this.props;
    return tree.map(node => {
      if (node.hasOwnProperty('children')) {
        return (
          <Node key={node.name} node={node} leafNodeClicked={this.leafNodeClicked}/>
        );
      } else {
        return (
          <Leaf key={node.name} leaf={node} leafNodeClicked={this.leafNodeClicked}/>
        )
      }
    })
  }

  render() {
    let { tree } = this.props;
    return (
      <div>
        {tree.length >= 1 && this.renderTree()}
      </div>
    )
  }
}

export default LeftTree;
