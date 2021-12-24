import * as React from 'react';
import Link from 'next/link'
import Box from '@mui/material/Box'
import AppBar from '@mui/material/AppBar'
import Toolbar from '@mui/material/Toolbar'
import IconButton from '@mui/material/IconButton'
import Typography from '@mui/material/Typography'
import Button from '@mui/material/Button'




export default function navbar() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar styles={{
                background: '#1976d2',
                color: 'white',
            }} position="static">
                <Toolbar>
                    <IconButton
                        size="large"
                        edge="start"
                        color="inherit"
                        aria-label="menu"
                        sx={{ mr: 2 }}
                    >
                    </IconButton>

                    <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
                        <Link href="/"> BSEG</Link>
                    </Typography>
                    {!isAuthenticated && <Link href="/login"><a>Sign In</a></Link>}
                    {/*{!isAuthenticated && <Link href="/signup"><a>Sign Up</a></Link>}*/}
                    {isAuthenticated && <li onClick={deauthenticate}><a>Sign Out</a></li>}
                </Toolbar>
            </AppBar>
        </Box>
    );
}