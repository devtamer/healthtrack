import React, { useState } from 'react';
import withRedux from 'next-redux-wrapper';
import axios from 'axios';
import { API } from '../config';
import initialize from '../utils/initialize';
import { initStore } from '../redux';
import router from 'next/router';
import HomeLayout from '../components/layouts/HomeLayout';


const Lab = ({ laborders }) => {

    return (
        <HomeLayout title={'Lab'}>
            <div style={{ display: "inline-block" }}>
                <div style={{ display: "flex" }}>
                    <h1 style={{ fontSize: "20px", fontWeight: "bold", paddingLeft: "40px", float: "left" }}>Lab Orders</h1>
                </div>
                <div className="update-patient" style={{ float: "left", paddingLeft: "40px", display: "inline-block" }}>
                    <form
                        onSubmit={"handleSubmit"}
                        className="container"
                        style={{
                            display: "flex",
                            flexFlow: "row wrap",
                            alignItems: "center",
                            width: '540px'
                        }}
                    >
                        <div className="style.field">
                            <p className="control has-icons-left has-icons-right">
                                <input
                                    style={{
                                        verticalAlign: "middle",
                                        margin: "5px 10px 5px 0",
                                        padding: "10px",
                                        backgroundColor: "#fff",
                                        border: "1px solid #ddd",
                                    }}
                                    type="text"
                                    placeholder="id"
                                    required
                                    value={"id"}
                                    onChange={e => setId(e.target.value)}
                                />
                                <span className="icon is-small is-left">
                                    <i className="fas fa-envelope" />
                                </span>
                                <span className="icon is-small is-right">
                                    <i className="fas fa-check" />
                                </span>
                            </p>
                        </div>
                        <div style={{ marginBottom: "0px" }} className="field">
                            <p className="control has-icons-left has-icons-right">
                                <input
                                    style={{
                                        verticalAlign: "middle",
                                        margin: "5px 10px 5px 0",
                                        padding: "10px",
                                        backgroundColor: "#fff",
                                        border: "1px solid #ddd",
                                    }}
                                    type="text"
                                    placeholder="id"
                                    required
                                    value={"id"}
                                    onChange={e => setId(e.target.value)}
                                />
                                <span className="icon is-small is-left">
                                    <i className="fas fa-envelope" />
                                </span>
                                <span className="icon is-small is-right">
                                    <i className="fas fa-check" />
                                </span>
                            </p>
                        </div>
                        <div style={{ display: "inline-block" }}>
                            <p className="control has-text-centered">
                                <button type="submit" className="button is-success">
                                    Update Patient Info
                                </button>
                            </p>
                        </div>
                    </form>
                </div>
                <div>
                    {!laborders
                        ?
                        <p>You are not signed in</p>
                        :
                        (<div style={{ margin: "auto", padding: "0 40px" }}>
                            <table style={{
                                margin: "auto", fontfamily: "arial, sans - serif",
                                borderCollapse: "collapse",
                                width: "100%",
                            }}>
                                <tr>
                                    <th className={{
                                        border: "1px solid #dddddd",
                                        textAlign: "left",
                                        padding: "8px",
                                    }}>ID</th>
                                    <th style={{ paddingLeft: "10px" }}>Date Performed</th>
                                    <th style={{ paddingLeft: "10px" }}>Patient Name</th>
                                    <th style={{ paddingLeft: "10px" }}>Performed By</th>
                                    <th style={{ paddingLeft: "10px" }}>Physician Name</th>
                                    <th style={{ paddingLeft: "10px" }}>Results</th>
                                    <th style={{ paddingLeft: "10px" }}>Test Type</th>
                                </tr>
                                {laborders.map(laborders => {
                                    return (
                                        <tr>
                                            <td>{laborders.date_performed}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.id}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.patient.first_name + ' ' +laborders.patient.last_name}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.performed_by}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.physician.first_name + ' ' + laborders.physician.last_name}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.results}</td>
                                            <td style={{ paddingLeft: "10px" }}>{laborders.test_type}</td>

                                        </tr>
                                    )
                                })}
                            </table>
                        </div>
                        )}
                </div>
            </div>

        </HomeLayout >


    )
};

Lab.getInitialProps = async (ctx) => {
    initialize(ctx);
    const token = ctx.store.getState().authentication.token;
    if (token) {
        const response = await axios.get(`${API}/laborder/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        }).catch(err => {
            console.log(err);
            return { err };
        });
        const laborders = await response.data['LAB ORDERS'];

        return { laborders, token };
    }

};


export default withRedux(initStore)(Lab);
