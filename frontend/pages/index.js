import React from 'react';
import axios from 'axios';
import withRedux from 'next-redux-wrapper';
import Link from 'next/link';
import { initStore } from '../redux';
import actions from '../redux/actions';
import { API } from '../config';
import initialize from '../utils/initialize';
import HomeLayout from '../components/layouts/HomeLayout';
import router from 'next/router';

class Index extends React.Component {


    render() {
        return (
            <HomeLayout title="Sign In">
                <div className="container">
                    <div className="row">
                        <h1> Home</h1>
                    </div>
                </div>
            </HomeLayout>
        );
    }
}

export default withRedux(initStore)(Index);
