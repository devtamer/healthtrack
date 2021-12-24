import withRedux from 'next-redux-wrapper';
import Link from 'next/link';
import { initStore } from '../redux';
import initialize from '../utils/initialize';
import HomeLayout from '../components/layouts/HomeLayout';
import router from 'next/router';


const dashboard = ({ token }) => {
  !token ? router.push('/login') : null;



  return (

    <HomeLayout>
      <body>
        <div style={{ height: '80vh' }}>
          <div style={{

            top: "50%",
            bottom: "0",
            left: "0",
            right: "0",
            display: "grid",
            gridTemplateColumns: "auto auto auto",
            margin: "auto",
            maxWidth: "800px",
            padding: "1em"
          }}>
            <Link href="/patients">
              <button style={{
                backgroundColor: "dodgerblue",
                border: "1px solid rgba(0, 0, 0, 0)",
                height: "100px",

                borderRadius: "5px",
                padding: "20px",
                height: "100px",
                color: "#FFF",
                fontSize: "30px",
                textAlign: "center",
                fontWeight: "bold",

                margin: "1em",
              }} class="grid-item">Patients</button></Link>
            <Link href="/lab"><button style={{
              backgroundColor: "dodgerblue",
              border: "1px solid rgba(0, 0, 0, 0)",
              height: "100px",
              color: "#FFF",
              borderRadius: "5px",
              padding: "20px",

              fontSize: "30px",
              textAlign: "center",
              margin: "1em",
              fontWeight: "bold",



            }} class="grid-item">Lab</button></Link>
            <Link href="/scheduler"><button style={{
              backgroundColor: "dodgerblue",
              border: "1px solid rgba(0, 0, 0, 0)",
              height: "100px",
              color: "#FFF",
              padding: "20px",
              fontSize: "30px",
              textAlign: "center",

              borderRadius: "5px",

              margin: "1em",
              fontWeight: "bold",


            }} class="grid-item">Scheduler</button></Link>
            <Link href="/pharmacy"><button style={{
              backgroundColor: "dodgerblue",
              border: "1px solid rgba(0, 0, 0, 0)",
              height: "100px",
              color: "#FFF",
              padding: "20px",
              fontSize: "30px",
              textAlign: "center",

              borderRadius: "5px",

              margin: "1em",
              fontWeight: "bold",


            }} class="grid-item">Pharmacy</button></Link>
            <Link href="/billing"><button style={{
              backgroundColor: "dodgerblue",
              border: "1px solid rgba(0, 0, 0, 0)",
              height: "100px",
              color: "#FFF",
              padding: "20px",
              fontSize: "30px",
              borderRadius: "5px",

              textAlign: "center",
              fontWeight: "bold",
              margin: "1em",

            }} class="grid-item">Billing</button></Link>
            <Link href="/equipment"><button style={{
              backgroundColor: "dodgerblue",
              border: "1px solid rgba(0, 0, 0, 0)",
              height: "100px",
              color: "#FFF",
              padding: "20px",
              borderRadius: "5px",
              fontSize: "30px",
              fontWeight: "bold",
              textAlign: "center",
              margin: "1em",

            }} class="grid-item">Equipment</button></Link>
          </div>
        </div>
      </body>



    </HomeLayout >
  );
}

dashboard.getInitialProps = async (ctx) => {
  initialize(ctx);
  const token = ctx.store.getState().authentication.token;
  return { token };

};

export default withRedux(initStore)(dashboard);
