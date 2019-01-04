'use strict';

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import * as $ from 'jquery';

class Polls extends React.Component {

	constructor(props) {
		super(props);
		this.state = {data:[]};
	}

	componentWillMount() {
		$.getJSON('/polls/api', '', (data) => this.setState({data}));			
	}

	render() {
		console.log('hi');
		return <div>
				{this.state.data.map(poll => <div key={poll.pk}>{poll.fields.question_text}</div>)}
		</div>
	}
}


function render() {
	ReactDOM.render(
	  	<Polls />,
	  	document.getElementById('reactAppRoot')
	);
}

render();