import React from 'react';

import Node from './node';
import Leaf from './leaf';


class LeftTree extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  renderTree() {
    let { tree } = this.props;
    return tree.map(node => {
      if (node.hasOwnProperty('children')) {
        return (
          <Node key={node.name} node={node}/>
        );
      } else {
        return (
          <Leaf key={node.name} leaf={node}/>
        )
      }
    })
  }

  render() {
    let { tree } = this.props;
    return (
      <div className="column left-tree">
        {tree.length >= 1 && this.renderTree()}
      </div>
    )
  }
}

export default LeftTree;
