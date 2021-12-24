
import actions from '../redux/actions';
import initialize from '../utils/initialize';
import { initStore } from '../redux';
import withRedux from 'next-redux-wrapper';
import axios from 'axios';
import { API } from '../config'
import HomeLayout from '../components/layouts/HomeLayout';
import router from 'next/router';

const Patients = ({ patientRecord, user}) => {
  return (
    < HomeLayout title="Patients" >

      <div style={{ display: "inline-block" }}>
        <div style={{ display: "flex" }}>
          <h1 style={{ fontSize: "20px", fontWeight: "bold", paddingLeft: "40px", float: "left" }}>Patients</h1>
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

        {!user
          ?
          <p>You are not signed in</p>
          :
          (<div style={{ margin: "auto", padding: "0 40px" }}>
            <table style={{
              margin: "auto", fontfamily: "arial, sans - serif",
              borderCollapse: "collapse",
              width: "100%", border: "1px solid #ddd",
            }}>
              <tr style={{ borderBottom: "2px solid #ddd" }} >
                <th style={{
                  paddingLeft: "4px",
                }}>ID</th>
                <th style={{ paddingLeft: "8px" }}>Name</th>
                <th style={{ paddingLeft: "8px" }}>Number</th>
                <th style={{ paddingLeft: "8px" }}>Email</th>
                <th style={{ paddingLeft: "8px" }}>Address</th>
                <th>Insurance</th>
                <th>DOB</th>
                <th style={{ paddingLeft: "8px" }}>Gender</th>
              </tr>
              {patientRecord.map(patient => {
                return (
                  <tr>
                    <td style={{ paddingLeft: "4px" }}>{patient.id}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.first_name + " " + patient.last_name}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.number}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.email}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.address}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.insurance}</td>
                    <td style={{ padding: "0 8px", borderRight: "1px solid #ddd" }}>{patient.dob}</td>
                    <td style={{ paddingLeft: "10px" }}>{patient.gender}</td>

                  </tr>
                )
              })}
            </table>
          </div>
          )}

      </div>


    </HomeLayout >
  )

}


Patients.getInitialProps = async (ctx) => {
  initialize(ctx);
  const token = ctx.store.getState().authentication.token;
  if (token) {
    const response = await axios.get(`${API}/records/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    })
    const user = await axios.get(`${API}/auth/status/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    });
    const patientRecord = await response.data["Patients"];
    if (response.status === 401) {
      ctx.store.dispatch({ type: "LOGOUT" });
    } else {
      return { patientRecord, user };
    }
  }
}


export default withRedux(initStore)(Patients);
