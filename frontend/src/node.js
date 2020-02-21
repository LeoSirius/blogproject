import React from 'react';

import Leaf from './leaf';


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

  leafNodeClicked = (leafNode) => {
    this.props.leafNodeClicked(leafNode)
  }

  render() {
    let { node } = this.props;
    let { isDisplayChildren } = this.state;
    return (
      <div className='node' onClick={this.toggleDisplayChildren}>
        {node.name}
        <div className={ isDisplayChildren ? '' :  'display-none'}>
        {node.children.map((node) => {
          if (node.hasOwnProperty('children')) {
            return (
              <Node key={node.name} node={node} leafNodeClicked={this.leafNodeClicked}/>
            )
          } else {
            return (
              <Leaf key={node.name} leaf={node} leafNodeClicked={this.leafNodeClicked}/>
            )
          }
        })}
        </div>
      </div>
    );
  }
}

export default Node;
