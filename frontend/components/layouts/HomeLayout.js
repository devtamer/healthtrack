import Link from 'next/link';
import Head from 'next/head';
import { connect } from 'react-redux';
import actions from '../../redux/actions';

const HomeLayout = ({ children, title, isAuthenticated, deauthenticate }) => (
  <div>
    <Head>
      <title>{title}</title>
      <meta charSet="utf-8" />
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css" />
    </Head>
    <div style={{ height: "80px", backgroundColor: "dodgerblue", boxShadow: "0 5px rgba(0,0,0,.1)" }} className="tabs is-centered">
      <ul style={{ borderBottom: "none" }}>
        <Link href="/dashboard"><a style={{ color: "#FFF", borderBottom: "none" }}>Home</a></Link>
        <Link href="/patients"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}>Patients</a></Link>
        <Link href="/lab"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}>Lab</a></Link>
        <Link href="/scheduler"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}> Scheduler</a></Link>

        <Link href="/pharmacy"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}>Pharmacy</a></Link>
        <Link href="/billing"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}>Billing</a></Link>
        <Link href="/equipment"><a style={{ color: "#FFF", marginLeft: "10px", borderBottom: "none" }}>Equipment</a></Link>
        <div style={{ marginLeft: "8vh" }}>
          {!isAuthenticated && <Link href="/login"><a style={{ color: "#FFF", border: "1px solid #FFF", borderRadius: "5px" }}>Sign In</a></Link>}
          {isAuthenticated && <li onClick={deauthenticate}><a style={{ color: "#FFF", border: "1px solid #FFF", borderRadius: "5px" }}>Sign Out</a></li>}
        </div>



      </ul>
    </div>

    <div className="has-text-centered">
      {children}
    </div>
    <div className="navbar-brand is-right">
      <a className="navbar-item is-hidden-desktop jb-navbar-menu-toggle" data-target="navbar-menu">
        <span className="icon"><i className="mdi mdi-dots-vertical"></i></span>
      </a>
    </div>
    <div style={{ backgroundColor: "dodgerblue", height: "50px" }} className="tabs is-centered">
      <ul>
        <Link href="/"><a style={{ color: "#FFF", borderBottom: "none" }}>Home</a></Link>
        <div style={{ marginLeft: "5vh" }}>
          {!isAuthenticated && <Link href="/login"><a style={{ color: "#FFF", borderBottom: "none" }}>Sign In</a></Link>}
          {isAuthenticated && <li onClick={deauthenticate}><a style={{ color: "#FFF" }}>Sign Out</a></li>}
        </div>



      </ul>
    </div>
  </div>
);

const mapStateToProps = (state) => (
  { isAuthenticated: !!state.authentication.token }
);

export default connect(mapStateToProps, actions)(HomeLayout);
