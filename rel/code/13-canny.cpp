void canny (Mat& A) {
    Mat B;
    if (sigma) {
        GaussianBlur (A, B, Size(0,0), sigma);
    } else
        A.copyTo(B);
    Gradient grad = get_gradient (B);
    Mat C;
    thin_edge (grad.G, C, grad.theta);
    float max_grad = get_max_grad (C);
    high_seuil = max_grad * (max_slider/100.0);
    low_seuil = max_grad * (min_slider/100.0);
    Mat D (C.rows, C.cols, CV_8U);
    BFS_edge_tracking (C, D);
    imshow ("Canny Algorithm", D);
}