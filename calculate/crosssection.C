void crosssection(){
    double Q2 = 0.1;
    double E_µ =1.5;
    double m_N = 0.94;
    double m_π = 0.14;
    double π = 3.14;
    double a = 1.0 / 137.0;
    //double F2 = 0.12;
    double F2 = 0.31;
    
    double W =1.25;
    
    double E_gamma = W * W / (2 * m_N);
    double y = E_gamma / E_µ;
    double x = Q2 / (2 * E_gamma * m_N);

    double Q2_min = m_π * m_π * y * y/ (1 - y);
    double sigma_tot = ( (4 * π * π* a ) / ( Q2 * (1 - x)) )  * ((Q2 + 4 * m_N * m_N * x * x) / Q2 ) * F2;

    double z = y + 0.3;

    double logQ = log(Q2 / Q2_min);
    double Q_minus = Q2_min * ((1 / Q2) - (1 / Q2_min) );
    double logy = log(z / y);
    double y_minus = z - y;
    double y2_minus = (z * z) - (y * y);
    double teisu = a /  π;

    double sigma_µN_GeV = sigma_tot * teisu * ( ( (logQ + Q_minus) * logy) - ((logQ + Q_minus) * y_minus) + (logQ * y2_minus /4) );
    double GeV_cm = 3.88 * std::pow(10, -26.0);
    double sigma_µN_cm = sigma_µN_GeV * GeV_cm;
    double sigma_µN_b = sigma_µN_cm * std::pow(10, 24);

    cout << "E_gamma: " << E_gamma << "GeV" << endl;
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout <<"Q2_min: " << Q2_min << "GeV^2" <<endl;
    cout << "sigma_µN_cm: " << sigma_µN_cm << "cm^2" << endl;
    cout << "sigma_µN_b: " << sigma_µN_b << "b" << endl;

    //calculate dN/dt

    double rho = 1.0;
    double N_A = 6.0 * std::pow(10, 23);
    double A = 1.0;
    double Pb = 2.0 * 2.0 * 40;

    double dNdt =  -rho * N_A * sigma_µN_cm * Pb / A;

    cout << "dN/dt: " << dNdt << "N" << endl;

}