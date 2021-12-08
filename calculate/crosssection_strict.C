void crosssection_strict(){
    double Q2 = 0.1;
    double E_mu =1.5;
    double m_N = 0.94;
    double m_pi = 0.14;
    double pi = 3.14;
    double a = 1.0 / 137.0;
    double F2 = 0.12;
    
    double W =1.25;
    
    double E_gamma = W * W / (2 * m_N);
    double y = E_gamma / E_mu;
    double x = Q2 / (2 * E_gamma * m_N);

    double Q2_min = m_pi * m_pi * y * y/ (1 - y);
    double sigma_tot = ( (4 * pi * pi * a ) / ( Q2 * (1 - x)) )  * ((Q2 + 4 * m_N * m_N * x * x) / Q2 ) * F2;

    double z = y + 0.3;
    double teisu = a / pi;
    double GeV_cm = 3.88 * std::pow(10, -26.0);
    double logQ = log(Q2 / Q2_min);
    double Q_minus = Q2_min * ((1 / Q2) - (1 / Q2_min) );
    double logy = log(z / y);
    double y_minus = z - y;
    double y2_minus = (z * z) - (y * y);

    int division_number = 10000000;
    double total_sigma_µN_cm = 0.0;
    double total_logQ2 = 0.0;
    double total_Q2_minus = 0.0;

    vector<double> part_sigma;

    for(int i =0; i < division_number; i++){
        //difine range of integration
        double Q2_differnce = Q2 - Q2_min;
        double left_range_Q = Q2_min + ( i * Q2_differnce / division_number );
        double right_range_Q =  Q2_min + ( (i + 1)  * Q2_differnce / division_number);

        double temp_logQ2 = log(right_range_Q / left_range_Q);
        double temp_Q2_minus = Q2_min * ((1 / right_range_Q) - (1/ left_range_Q) );

        total_logQ2 += temp_logQ2;
        total_Q2_minus += temp_Q2_minus;
    }

    for(int i=0;i < division_number;i++){
        double y_difference = z - y;
        double left_range_y = y + ( i * y_difference / division_number );
        double right_range_y = y + ( (i + 1 ) * y_difference / division_number);

        double temp_logy = log(right_range_y / left_range_y);
        double temp_y_minus = right_range_y - left_range_y  ;
        double temp_y2_minus = (right_range_y * right_range_y) - (left_range_y * left_range_y) ;

        double partially_sigma_µN_GeV = sigma_tot * teisu * (( (total_logQ2 + total_Q2_minus) * temp_logy) - ((total_logQ2 + total_Q2_minus) * temp_y_minus) + (total_logQ2 * temp_y2_minus /4) );
        double temp_partially_sigma_µN_cm = partially_sigma_µN_GeV * GeV_cm;
        part_sigma.push_back(temp_partially_sigma_µN_cm);
        total_sigma_µN_cm += temp_partially_sigma_µN_cm;   
    }

    double sigma_µN_GeV = sigma_tot * teisu * ( ( (logQ + Q_minus) * logy) - ((logQ + Q_minus) * y_minus) + (logQ * y2_minus /4) );
    double sigma_µN_cm = sigma_µN_GeV * GeV_cm;

    //cout << "E_gamma = " << E_gamma << "GeV" << endl;
    //cout << "x = " << x << endl;
    //cout << "y = " << y << endl;
    //cout <<"Q2_min = " << Q2_min << "GeV^2" <<endl;
    cout << "sigma_µN_cm^2 = " << sigma_µN_cm << "cm^2" << endl;
    cout << "total_sigma_µN_cm = " << total_sigma_µN_cm  << "cm^2" << endl;

    //calculate dN/dt

    double rho = 1.0;
    double N_A = 6.0 * std::pow(10, 23);
    double A = 1.0;
    double Pb = 2.0 * 2.0 * 40;

    double dNdt_rough =  -rho * N_A * sigma_µN_cm * Pb / A;
    double dNdt_integation = -rho * N_A * total_sigma_µN_cm * Pb / A;

    cout << "dN/dt rough = " << dNdt_rough << "N" << endl;
    cout << "dN/dt intrgation = " << dNdt_integation << "N" << endl;
}