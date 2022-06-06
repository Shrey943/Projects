package com.example.credence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        Button newBelief = findViewById(R.id.newBelief);
        Button credences = findViewById(R.id.credences);

        newBelief.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(HomeActivity.this,MainActivity.class);
                intent.putExtra("frag2","0");
                startActivity(intent);
            }
        });
        credences.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent1 = new Intent(HomeActivity.this,MainActivity.class);
                intent1.putExtra("frag2","1");
                startActivity(intent1);
            }
        });

    }
}