/*eslint-disable*/
import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@material-ui/core";
import { Container } from '@mui/material';


export default function Footer() {
    return (
        <AppBar position="static" color="primary">
            <Container maxWidth="md">
                <Toolbar>
                    <Typography variant="body1" color="inherit">
                        © 2021 BSEG
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    )
}
