package com.example.credence;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.res.ColorStateList;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.tabs.TabLayout;

import androidx.viewpager.widget.ViewPager;
import androidx.appcompat.app.AppCompatActivity;

import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toolbar;

import com.example.credence.ui.main.SectionsPagerAdapter;

public class MainActivity extends AppCompatActivity {

    @SuppressLint("ResourceAsColor")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager());
        ViewPager viewPager = findViewById(R.id.view_pager);
        viewPager.setAdapter(sectionsPagerAdapter);
        TabLayout tabs = findViewById(R.id.tabs);
        tabs.setupWithViewPager(viewPager);
        tabs.setSelectedTabIndicatorColor(getResources().getColor(R.color.white));
//       tabs.setTabTextColors(ColorStateList.valueOf(getResources().getColor(R.color.demand)));
        try {
            Intent intent10 = getIntent();
            String frag =  intent10.getStringExtra("frag2");
            tabs.getTabAt(Integer.parseInt(frag)).select();


        }catch (Exception e){}

//        getSupportActionBar().setLogo(R.drawable.);
//        Toolbar myToolBar = (Toolbar) findViewById(R.id.mCustomToolbar);



    }
}