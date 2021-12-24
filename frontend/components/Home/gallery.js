import React from "react";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

export default function Gallery() {
    const cards = [1, 2, 3];

    return (
        <main>
            <Box sx={{ bgcolor: 'background.paper', pt: 8, pb: 6 }}>
                <Container maxWidth="sm">
                    <Typography
                        component="h2"
                        variant="h4"
                        align="left"
                        color="text.primary"
                        gutterBottom
                    >
                        Our Mission
                    </Typography>
                    <Typography variant="h5" align="left" color="text.secondary" paragraph>
                        We provide professional and paraprofessional services in the community, assisting individuals to achieve their highest quality of life. We are committed to providing high quality multidisciplinary care, by professionals who recognize the need for comprehensive assessment of needs from both the patients and the professional's point of view
                    </Typography>
                </Container>
            </Box >
            <Container sx={{ py: 8, marginTop: '-10vh', marginBottom: '10vh' }} maxWidth="md">
                {/* End hero unit */}
                <Grid container spacing={4}>
                    {cards.map((card) => (
                        <Grid item key={card} xs={12} sm={6} md={4}>
                            <Card
                                sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                            >
                                <CardMedia
                                    component="img"
                                    // sx={{

                                    //     pt: '10.25%',
                                    // }}
                                    image="https://previews.123rf.com/images/wavebreakmediamicro/wavebreakmediamicro1507/wavebreakmediamicro150702614/42225780-smiling-patient-looking-at-camera-with-doctors-behind-in-hospital-room.jpg"
                                    alt="random"
                                />
                                <CardContent sx={{ flexGrow: 1 }}>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        Heading
                                    </Typography>
                                    <Typography>
                                        This is a media card. You can use this section to describe the
                                        content.
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </Container>
        </main>
    )
}